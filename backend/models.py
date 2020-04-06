from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Device(models.Model):
    device_name = models.CharField(max_length=50)
    device_description = models.TextField(null=True, blank=True)
    device_project = models.ForeignKey(Project, on_delete=models.CASCADE)


class SensorType(models.Model):
    def __str__(self):
        return self.sensor_type

    sensor_type = models.CharField(max_length=100)


class Distribution(models.Model):
    def __str__(self):
        return self.distribution

    distribution = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default='NA')


class Sensor(models.Model):
    sensor_device = models.ForeignKey(Device, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    sensor_distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE)
    outliers_amount = models.IntegerField(default=0)
    lines_amount = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)


class DistributionParameters(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)


class Report(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_ready = models.BooleanField(default=False)


class ReportSensorType(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)


class Record(models.Model):
    # запись в таблице, используется для построения отчета
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time = models.DateTimeField()
    value = models.FloatField()
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
