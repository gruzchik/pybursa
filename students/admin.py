# -*- coding: utf-8 -*-
from django.contrib import admin

from students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'package']
    list_display_links = ['first_name', 'last_name', 'package']
    list_filter = ['first_name', 'last_name',
        'package']
    search_fields = ['first_name', 'last_name', 'package']
    filter_horizontal = ['courses']
    radio_fields = {"package": admin.HORIZONTAL}
