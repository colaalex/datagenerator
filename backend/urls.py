from django.urls import path

from .views import *

# список урлов, по которым пользователь обращается к приложению 
# (просмотр проектов, отчетов)

urlpatterns = [
    path('tokensign/', tokensign),
    path('create_project/', create_project),
    path('delete_project/<int:p_id>/', delete_project),
    path('create_device/<int:p_id>/', create_device),
    path('delete_device/<int:d_id>/', delete_device),
    path('get_sensors/<int:d_id>/', get_sensors),
    path('create_sensor/<int:d_id>/', create_sensor),
    path('delete_sensor/<int:s_id>/', delete_sensor),
    path('generate/<int:s_id>', generate),
    path('generate_device/<int:d_id>/', generate_device),
    path('edit_project/<int:p_id>/', edit_project),
    path('edit_device/<int:d_id>/', edit_device),
    path('create_report/<int:p_id>/', create_report),
    path('plot_data/<int:report_id>/<int:sensor_type_id>/', plot_data)
]
