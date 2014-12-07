from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import students_list, students_item


urlpatterns = patterns('',
    url(r'^$', students_list),
    url(r'^(?P<student_id>\d+)/$', students_item),
)
