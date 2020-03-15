from django.urls import path

from .views import test, generate, tokensign

urlpatterns = [
    path('test/', test),
    path('generate/', generate),
    path('tokensign/', tokensign)
]