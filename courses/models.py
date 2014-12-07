from django.db import models

# Create your models here.

class Course(models.Model):
    technology = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    lector = models.CharField(max_length=255)
    asistant = models.CharField(max_length=255)
    start_date = models.DateField()
    finish_date = models.DateField()
