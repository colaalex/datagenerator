from django.shortcuts import render


def start(request, *args):
    return render(request, 'index.html')


def generator(request, *args):
    return render(request, 'main.html')
