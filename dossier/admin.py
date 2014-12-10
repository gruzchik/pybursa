from django.contrib import admin
from dossier.models import Dossier

# Register your models here.

#class AddressAdmin(admin.ModelAdmin):
 #   list_display = ('country', 'region', 'street', 'numbuild')

admin.site.register(Dossier)#, AddressAdmin)