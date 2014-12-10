from django.contrib import admin

# Register your models here.
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'ctype')

admin.site.register(Coach, CoachAdmin)