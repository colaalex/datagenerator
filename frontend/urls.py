from django.urls import path

from .views import *

urlpatterns = [
    path('', start),
    path('generator/', generator),
    path('project/<int:p_id>/', show_project)
]
