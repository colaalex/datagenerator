from .models import Report, Sensor, SensorType, DistributionParameters

from .externals.libs.datagenerator import datagen
from .externals.libs.datagenerator.main import time_to_rows

import datetime as dt


def prepare_report(report_id):
    report = Report.objects.get(pk=report_id)
    time_start = report.start_time.strftime('%Y-%m-%d %H:%M:%S')
    time_end = report.end_time.strftime('%Y-%m-%d %H:%M:%S')
    period = dt.timedelta(days=0, hours=1, minutes=0, seconds=0)
    devices = report.devices.all()
    sensor_types = {}  # {'sensor_type (id)': [sensors]}

    rows, start, period = time_to_rows(time_start, time_end, '0 1 0 0')

    for d in devices:
        sensors = Sensor.objects.filter(sensor_device=d).all()
        for s in sensors:
            if s.sensor_type.id not in sensor_types:
                sensor_types[s.sensor_type] = [s]
            # sensor_types.add(s.sensor_type.id)

    for st in sensor_types:
        for s in sensor_types[st]:
            dist_params = DistributionParameters.objects.filter(sensor_id=s).all()
            types = ['daterow', s.sensor_distribution.code]
            params = [[start, period], [float(i.value) for i in dist_params]]
            dg = datagen.DataGenerator(types=types, params=params, size=rows)
            data = dg.count()

            print(data)


# prepare_report(2)
