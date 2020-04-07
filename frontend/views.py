from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import render

from backend.models import Project, Device, Report, ReportSensorType


# данные для CLIENT_ID хранятся в secret.py


def start(request, *args):
    # главная стрница
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    projects = None
    if request.user.is_authenticated:
        projects = Project.objects.filter(project_owner=request.user).all()
    return render(request, 'index.html', {'client': CLIENT_ID, 'projects': projects, 'project': None})


def show_project(request, p_id, *args):
    # страница проекта
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    project = Project.objects.get(pk=p_id)
    reports = Report.objects.filter(project_id=p_id).all()
    if request.user.is_authenticated and request.user == project.project_owner:
        projects = Project.objects.filter(project_owner=request.user).all()
        devices = Device.objects.filter(device_project=project).all()
        return render(request, 'index.html', {
            'client': CLIENT_ID, 'projects': projects, 'project': project, 'devices': devices, 'reports': reports})
    else:
        return HttpResponseForbidden()


def show_report(request, r_id, *args):
    # страница отчета
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    report = Report.objects.get(pk=r_id)
    if request.user != report.project.project_owner:
        return HttpResponseForbidden()
    project = report.project
    reports = Report.objects.filter(project=project).all()
    projects = Project.objects.filter(project_owner=request.user).all()
    stypes = ReportSensorType.objects.filter(report=report).all()
    return render(request, 'report.html', {
        'client': CLIENT_ID, 'projects': projects, 'project': project, 'report': report, 'reports': reports, 'stypes': stypes})
