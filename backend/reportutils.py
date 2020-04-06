from .models import Report, Sensor, SensorType, DistributionParameters, Record, ReportSensorType

from .externals.libs.datagenerator import datagen
from .externals.libs.datagenerator.main import time_to_rows

import datetime as dt
from numpy import mean, median


def prepare_report(report_id):
    report = Report.objects.get(pk=report_id)
    time_start = report.start_time.strftime('%Y-%m-%d %H:%M:%S')
    time_end = report.end_time.strftime('%Y-%m-%d %H:%M:%S')
    period = '0 1 0 0'
    devices = report.devices.all()
    sensor_types = {}  # {'sensor_type (id)': [sensors]}

    rows, start, period = time_to_rows(time_start, time_end, period)

    for d in devices:
        sensors = Sensor.objects.filter(sensor_device=d).all()
        for s in sensors:
            if s.sensor_type not in sensor_types:
                sensor_types[s.sensor_type] = [s]
                ReportSensorType(sensor_type=s.sensor_type, report=report).save()
            else:
                sensor_types[s.sensor_type].append(s)
            # sensor_types.add(s.sensor_type.id)

    for st in sensor_types:
        for s in sensor_types[st]:
            dist_params = DistributionParameters.objects.filter(sensor_id=s).all()
            types = ['daterow', 'temperature']
            params = [[start, period], [float(i.value) for i in dist_params]]
            dg = datagen.DataGenerator(types=types, params=params, size=rows)
            data = dg.count()

            for i in data:
                record = Record(report=report, sensor=s, time=i[0], value=i[1], sensor_type=st)
                record.save()


def plotly_data(report_id, sensor_type_id):
    # sensors = Sensor.objects.filter(record__report_id=report_id, record__sensor_type_id=sensor_type_id).all()
    records = Record.objects.filter(report_id=report_id, sensor_type_id=sensor_type_id).all()
    traces = {}  # {s_id: {'x': x, 'y': [values], 'type': 'scatter', 'name': name, 'x': [time]}}
    raw_values = []  # все подряд значения для статистики
    for r in records:
        if r.sensor.id not in traces:
            traces[r.sensor.id] = {'type': 'scatter', 'y': [r.value], 'name': r.sensor.sensor_device.device_name, 'x': [r.time.strftime('%H:%M')]}
        else:
            traces[r.sensor.id]['y'].append(r.value)
            traces[r.sensor.id]['x'].append(r.time.strftime('%H:%M'))
        raw_values.append(r.value)
    data = []
    for t in traces:
        data.append(traces[t])

    report_text = f'Максимальное значение: {max(raw_values)}\nМинимальное значение: {min(raw_values)}\n' \
                  f'Среднее значение: {mean(raw_values)}\nМедианное значение: {median(raw_values)}'

    return {'data': data, 'text': report_text}
