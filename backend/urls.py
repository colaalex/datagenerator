from django.urls import path

from .views import *

urlpatterns = [
    path('test/', test),
    path('generate/<int:s_id>', generate),
    path('tokensign/', tokensign),
    path('create_project/', create_project),
    path('delete_project/<int:p_id>/', delete_project),
    path('create_device/<int:p_id>/', create_device),
    path('delete_device/<int:d_id>/', delete_device),
    path('get_sensors/<int:d_id>/', get_sensors),
    path('create_sensor/<int:d_id>/', create_sensor),
    path('delete_sensor/<int:s_id>/', delete_sensor),
    path('generate_device/<int:d_id>/', generate_device),
    path('edit_project/<int:p_id>/', edit_project),
    path('create_report/<int:p_id>/', create_report),
]
