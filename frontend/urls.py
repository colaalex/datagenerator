from django.urls import path

from .views import start, generator

urlpatterns = [
    path('', start),
    path('generator/', generator)
]
