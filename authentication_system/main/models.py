from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class student(models.Model):
    name = models.CharField(("Name of Student"),max_length=40,unique=False,)
    work_to_do =  models.TextField(("Assign Some Work"),max_length=1000,unique=False)
    deadline = models.DateField(default=timezone.now,unique=False)

    def __str__(self):

        return self.name
