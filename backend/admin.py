from django.contrib import admin

from .models import *


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Device)
admin.site.register(Distribution)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(DistributionParameters)
admin.site.register(Report)
admin.site.register(Record)
admin.site.register(ReportSensorType)
