from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
