from django.db import models

# Create your models here.

class Address(models.Model):
    postindex = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    disctrict = models.CharField(max_length=13, blank=True)
    street = models.CharField(max_length=255)
    numbuild = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "%s %s" % (self.postindex, self.country)