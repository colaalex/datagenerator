from django.urls import path

from .views import test, generate

urlpatterns = [
    path('test/', test),
    path('generate/', generate),
]