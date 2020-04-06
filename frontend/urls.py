from django.urls import path

from .views import show_project, show_report, start

urlpatterns = [
    path('', start),
    path('project/<int:p_id>/', show_project),
    path('report/<int:r_id>/', show_report),
]
