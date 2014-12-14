from django.contrib import admin

from address.models import Address


# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'region', 'street']
    list_display_links = ['country', 'region', 'street']
    list_filter = ['country', 'region',
        'street', 'numbuild']
    search_fields = ['country', 'region', 'street', 'numbuild']
