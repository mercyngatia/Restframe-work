from __future__ import unicode_literals
from django.db import models

import datetime


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    description=models.TextField(max_length= 50)
    availability=models.TextField(max_length=50)
    registration_date=models.DateField(default=datetime.date.today())
    graduation_date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name
        
        
        