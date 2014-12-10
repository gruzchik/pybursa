from django.contrib import admin

from address.models import Address


# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'region', 'street', 'numbuild')

admin.site.register(Address, AddressAdmin)
