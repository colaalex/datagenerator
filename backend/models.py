from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    """
    Модель проекта.

    project_name - название проекта (отображается на странице)

    project_description - описание проекта (отображается на странице)

    project_owner - владелец проекта, тот, кто создал
    """
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Device(models.Model):
    """
    Модель устройства.

    device_name - название устройства (отображается на странице)

    device_description — описание устройства (отображается на странице)

    device_project - проект, которому принадлежит устройство
    """
    device_name = models.CharField(max_length=50)
    device_description = models.TextField(null=True, blank=True)
    device_project = models.ForeignKey(Project, on_delete=models.CASCADE)


class SensorType(models.Model):
    """
    Справочная модель (в БД хранятся типы датчиков в виде текста)

    Например: термометр, датчик освещения и т.д.
    """
    def __str__(self):
        return self.sensor_type

    sensor_type = models.CharField(max_length=100)


class Distribution(models.Model):
    """
    Справочная модель (в БД хранятся типы распределений в виде текста
    и его кода). Необходимо для связи того, что видит пользователь, 
    и как это передается во внутренние функции.

     Например: distribution='Бета', code='beta'
    """
    def __str__(self):
        return self.distribution

    distribution = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default='NA')


class Sensor(models.Model):
    """
    Модель датчика, поля:

    sensor_device — устройство, которому принадлежит датчик, внешний ключ (Device), обязательное поле;
    
    sensor_name — название датчика, текст до 50 символов, обязательное поле;
    
    sensor_type — тип датчика, внешний ключ (SensorType), обязательное поле;
    
    sensor_distribution — тип распределения, по котрому датчик будет генерировать данные, внешний ключ (Distribution), обязательное поле;
    
    outliers_amount — количество выбросов, целое число, обязательное поле;
    
    lines_amount — количество строк, которые будут сгенерированы датчиком, целое число, необязательное поле;
    
    start_time — время начала отсчета, используется при генерации данных, дата и время, необязательное поле;
    
    end_time — время окончания отсчета, используется при генерации данных, дата и время, необязательное поле;
    
    period — периодичность отсчетов, используется при генерации данных по времени, строка формата «d h m s», где d, h, m, s — целые числа, обозначающие периодичность в днях, часах, минутах и секундах соответственно;

    """
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
    """
    Модель параметров распределений, задается пользователем при создании датчика, поля:
    
    sensor — датчик, для которого задан параметр, внешний ключ (Sensor), обязательное поле;
    
    value — значение параметра, вещественное число, обязательное поле;
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)


class Report(models.Model):
    """
    Модель параметров распределений, задается пользователем при создании датчика, поля:
    
    sensor — датчик, для которого задан параметр, внешний ключ (Sensor), обязательное поле;
    
    value — значение параметра, вещественное число, обязательное поле;
    """
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_ready = models.BooleanField(default=False)


class ReportSensorType(models.Model):
    """
    Модель типа датчика, используемого в отчете, поля:
    
    report — какому отчету принадлежит тип датчика, внешний ключ (Report), обязательное поле;
    
    sensor_type — тип датчика, внешний ключ (SensorType), обязательное поле;
    """
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)


class Record(models.Model):
    """
    Модель типа датчика, используемого в отчете, поля:
    
    report — какому отчету принадлежит тип датчика, внешний ключ (Report), обязательное поле;
    
    sensor_type — тип датчика, внешний ключ (SensorType), обязательное поле;
    """
    # запись в таблице, используется для построения отчета
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time = models.DateTimeField()
    value = models.FloatField()
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
