from django.db import models

# Create your models here.

class Employee_Info(models.Model):
    full_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='emp_profile')
    position = models.CharField(max_length=20)
    address = models.CharField(max_length=100)