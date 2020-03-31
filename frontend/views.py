from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import render

from backend.models import Project, Device


def start(request, *args):
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    projects = None
    if request.user.is_authenticated:
        projects = Project.objects.filter(project_owner=request.user).all()
    return render(request, 'index.html', {'client': CLIENT_ID, 'projects': projects, 'project': None})


def show_project(request, p_id, *args):
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    project = Project.objects.get(pk=p_id)
    if request.user.is_authenticated and request.user == project.project_owner:
        projects = Project.objects.filter(project_owner=request.user).all()
        devices = Device.objects.filter(device_project=project).all()
        return render(request, 'index.html', {
            'client': CLIENT_ID, 'projects': projects, 'project': project, 'devices': devices})
    else:
        return HttpResponseForbidden()
