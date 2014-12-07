from django.db import models

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    position = models.CharField(max_length=25)
    position_choices = (
        ('Lector', 'Lector'),
        ('Asistant', 'Asistant'),
    )
    position_adv = models.CharField(max_length=25, choices=position_choices, default='Lector')
    course_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
