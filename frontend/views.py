from django.conf import settings
from django.shortcuts import render


def start(request, *args):
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    return render(request, 'index.html', {'client': CLIENT_ID})


def generator(request, *args):
    return render(request, 'main.html')
