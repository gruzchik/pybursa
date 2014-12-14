from django.contrib import admin
from dossier.models import Dossier

# Register your models here.

#class AddressAdmin(admin.ModelAdmin):
 #   list_display = ('country', 'region', 'street', 'numbuild')

#admin.site.register(Dossier)#, AddressAdmin)

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_display = ['address', 'like_color']
    list_display_links = ['address', 'like_color']
    list_filter = ['address', 'like_color']
    search_fields = ['address']
    filter_horizontal = ['hate_course']
    radio_fields = {'like_color': admin.HORIZONTAL}