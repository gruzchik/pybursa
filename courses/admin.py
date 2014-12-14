from django.contrib import admin

# Register your models here.
from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'technology', 'start_date', 'end_date']
    list_display_links = ['name', 'technology', 'start_date', 'end_date']
    list_filter = ['name', 'technology',
        'start_date', 'end_date']
    search_fields = ['name', 'technology']
    prepopulated_fields = {'slug': ('name',)}
    radio_fields = {'technology': admin.HORIZONTAL}
