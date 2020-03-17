from django.urls import path

from .views import *

urlpatterns = [
    path('test/', test),
    path('generate/', generate),
    path('tokensign/', tokensign),
    path('create_project/', create_project),
    path('delete_project/<int:p_id>/', delete_project)
]