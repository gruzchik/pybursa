from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
#    package = models.CharField(max_length=15, default='st')
    package_choises = (
        ('st', 'Standart'),
        ('gl', 'Gold'),
        ('vp', 'VIP'),
    )
    package_adv = models.CharField(max_length=15, choices=package_choises, default='st')
