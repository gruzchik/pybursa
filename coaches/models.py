from django.contrib.auth.models import User
from django.db import models
from dossier.models import Dossier

class Coach(models.Model):
    COACH_TYPES = (('Coach', 'Coach'), ('Assistant', 'Assistant'))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    ctype = models.CharField(choices=COACH_TYPES, max_length=1)
    user = models.ForeignKey(User)
    dossier = models.OneToOneField(Dossier, blank=True, null=True)

    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.ctype)


