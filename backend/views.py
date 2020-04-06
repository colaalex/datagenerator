from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.conf import settings
from django.contrib.auth import login
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from google.oauth2 import id_token
from google.auth.transport import requests
# import requests

import json
import logging
from uuid import uuid1

from .externals.libs.datagenerator import main as dg
from .models import User, Project, Device, Sensor, DistributionParameters, Distribution, Report
from .reportutils import prepare_report, plotly_data
from .forms import ProjectCreateForm


logger = logging.getLogger(__name__)


def test(request, *args, **kwargs):
    dg.mainf('test', 10, ['h1', 'h2', 'h3'], ["normal", "triangular", "beta"], [[0, 12], [5, 10, 15], [10, 20]], 10)
    return HttpResponse('OK')


# @csrf_protect
@require_POST
def tokensign(request, *args):
    token = request.POST.get('idtoken', None)
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer')

        userid = idinfo['sub']
        first_name = idinfo['given_name']
        last_name = idinfo['family_name']
        email = idinfo['email']

        if User.objects.filter(username=userid).exists():
            user = User.objects.get(username=userid)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        else:
            user = User(username=userid, first_name=first_name, last_name=last_name, email=email)
            user.set_unusable_password()
            user.save()
            login(request, user)
        return HttpResponse(userid)
    except ValueError as e:
        return HttpResponse(e)


@require_GET
def generate(request, s_id, *args):
    filename = f'data_{s_id}_{uuid1()}'
    sensor = Sensor.objects.get(pk=s_id)
    headers = [sensor.sensor_name]
    types = [sensor.sensor_distribution.code]
    dist_params = DistributionParameters.objects.filter(sensor=sensor).all()
    params = [[float(i.value) for i in dist_params]]
    rows = sensor.lines_amount
    try:
        time_start = sensor.start_time.strftime('%Y-%m-%d %H:%M:%S')
        time_end = sensor.end_time.strftime('%Y-%m-%d %H:%M:%S')
    except AttributeError:
        time_start, time_end = None, None
    period = sensor.period

    dg.mainf(filename=filename, headers=headers, types=types, params=params, rows=rows, time_start=time_start, time_end=time_end, period=period)

    return HttpResponse(filename)


@require_POST
def create_project(request, *args):
    # form = ProjectCreateForm(request.POST)
    # if form.is_valid():
    user = request.user
    name = request.POST.get('project-name')
    description = request.POST.get('project-text')
    project = Project(project_name=name, project_description=description, project_owner=user)
    project.save()

    return HttpResponseRedirect('/')
    # else:
    #     return HttpResponseBadRequest()


def delete_project(request, p_id, *args):
    user = request.user
    project = Project.objects.get(pk=p_id)
    if project.project_owner == user:
        project.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseForbidden()


@require_POST
def create_device(request, p_id, *args):
    project = Project.objects.get(pk=p_id)
    if request.user != project.project_owner:
        return HttpResponseForbidden()
    device_name = request.POST.get('device-name')
    device_text = request.POST.get('device-text')
    device = Device(device_name=device_name, device_description=device_text, device_project=project)
    device.save()
    return HttpResponseRedirect(f'/project/{p_id}')


def delete_device(request, d_id, *args):
    device = Device.objects.get(pk=d_id)
    project = device.device_project
    if request.user != project.project_owner:
        return HttpResponseForbidden()
    device.delete()
    return HttpResponseRedirect(f'/project/{project.id}')


def get_sensors(request, d_id, *args):
    sensors = Sensor.objects.filter(sensor_device_id=d_id).all()
    data = serializers.serialize('json', sensors)
    return JsonResponse(data, safe=False)


@require_POST
def create_sensor(request, d_id, *args):
    # TODO проверка на юзера
    parameters = json.loads(list(request.POST.dict().keys())[0])
    logger.error(parameters)
    name = parameters.get('sensor-create-name')
    sensor_type = int(parameters.get('inputState', 0))
    sensor_distribution = Distribution.objects.filter(code=parameters.get('inputdistribution')).get()
    sensor_outlier = parameters.get('sensor-create-outlier', 0)
    sensor_lines = parameters.get('sensor-create-lines', None)
    sensor_time_start = parameters.get('sensor-create-time-start', None)
    sensor_time_start = None if sensor_time_start == "" else sensor_time_start
    sensor_time_stop = parameters.get('sensor-create-time-stop', None)
    sensor_time_stop = None if sensor_time_stop == "" else sensor_time_stop
    sensor_time_period_days = parameters.get('sensor-create-time-period-days', None)
    sensor_time_period_time = parameters.get('sensor-create-time-period-time', None)
    try:
        period = sensor_time_period_days + ' ' + sensor_time_period_time
    except TypeError:
        period = None
    if period == "":
        period = None
    sensor = Sensor(sensor_device_id=d_id, sensor_name=name, sensor_type_id=sensor_type, sensor_distribution=sensor_distribution, outliers_amount=sensor_outlier, lines_amount=sensor_lines, start_time=sensor_time_start, end_time=sensor_time_stop, period=period)
    sensor.save()
    param1 = parameters.get('distribution-param-1')
    param2 = parameters.get('distribution-param-2', None)
    param3 = parameters.get('distribution-param-3', None)
    DistributionParameters(sensor=sensor, value=param1).save()
    if param2 is not None:
        DistributionParameters(sensor=sensor, value=param2).save()
    if param3 is not None:
        DistributionParameters(sensor=sensor, value=param3).save()
    return get_sensors(request, d_id)


def delete_sensor(request, s_id, *args):
    sensor = Sensor.objects.get(pk=s_id)
    if sensor.sensor_device.device_project.project_owner != request.user:
        return HttpResponseForbidden()
    sensor.delete()
    return HttpResponse('OK')


def generate_device(request, d_id, *args):
    # TODO проверка на юзера
    sensors = Sensor.objects.filter(sensor_device_id=d_id).all()
    # filename, headers, types, params, rows = None, time_start = None, time_end = None, period = None, chunk_size = 10000
    filename = f'data_d{d_id}_{uuid1()}'
    logger.error(request.POST)
    parameters = json.loads(list(request.POST.dict().keys())[0])
    lines = parameters.get('sensor-create-lines', None)
    lines = int(lines) if lines is not None else None
    time_start = parameters.get('sensor-create-time-start', None)
    time_start = None if time_start == "" else time_start
    time_stop = parameters.get('sensor-create-time-stop', None)
    time_stop = None if time_stop == "" else time_stop
    time_period_days = parameters.get('sensor-create-time-period-days', None)
    time_period_time = parameters.get('sensor-create-time-period-time', None)
    try:
        period = time_period_days + ' ' + time_period_time
    except TypeError:
        period = None
    if period == "":
        period = None

    headers = []
    types = []
    dist_params = []
    params = []
    for s in sensors:
        headers.append(s.sensor_name)
        types.append(s.sensor_distribution.code)
        dp = DistributionParameters.objects.filter(sensor=s).all()
        dist_params.append(dp)
        params.append([float(i.value) for i in dp])

    dg.mainf(filename=filename, headers=headers, types=types, params=params, rows=lines, time_start=time_start, time_end=time_stop, period=period)

    return HttpResponse(filename)


@require_POST
def edit_project(request, p_id, *args):
    user = request.user
    project = Project.objects.get(pk=p_id)
    if user != project.project_owner:
        return HttpResponseForbidden()
    name = request.POST.get('project-name')
    description = request.POST.get('project-text')
    project.project_name = name
    project.project_description = description
    project.save()

    return HttpResponseRedirect(f'/project/{p_id}')


def create_report(request, p_id, *args):
    user = request.user
    project = Project.objects.get(pk=p_id)
    if user != project.project_owner:
        return HttpResponseForbidden()
    logger.error(request.POST)
    name = request.POST.get('report-create-name')
    devices = request.POST.getlist('report-select-devices')
    time_start = request.POST.get('report-time-start')
    time_end = request.POST.get('report-time-end')

    report = Report(name=name, start_time=time_start, end_time=time_end, project=project)
    report.save()

    for d_id in devices:
        report.devices.add(Device.objects.get(pk=d_id))

    # TODO вынести в фон
    prepare_report(report.id)

    return HttpResponseRedirect(f'/project/{p_id}')


def plot_data(request, report_id, sensor_type_id, *args):
    data = plotly_data(report_id, sensor_type_id)
    return JsonResponse(data)
