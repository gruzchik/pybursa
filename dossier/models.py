from django.db import models
#from courses.models import Course
from address.models import Address

# Create your models here.

class Dossier(models.Model):
    #info = models.CharField(max_length=255)
    COLOR_CHOICES = (
        ('r', 'red'),
        ('o', 'orange'),
        ('y', 'yellow'),       
        ('g', 'green'),
        ('b', 'blue'),
        ('p', 'purple'),
        ('w', 'white'),

    )
    address = models.ForeignKey('address.Address', blank=True, null=True)
    hate_course = models.ManyToManyField('courses.Course', blank=True, null=True)
    like_color = models.CharField(max_length=1, choices=COLOR_CHOICES,
                               default='g')

        
    def __unicode__(self):
        return "%s %s" % (self.postindex, self.country)
