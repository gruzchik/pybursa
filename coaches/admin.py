from django.contrib import admin

# Register your models here.
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'ctype']
    list_display_links = ['first_name', 'last_name', 'ctype']
    list_filter = ['first_name', 'last_name',
        'ctype']
    search_fields = ['first_name', 'last_name', 'ctype']
    if len(Coach.COACH_TYPES) <= 5:
        radio_fields = {'ctype': admin.HORIZONTAL}
