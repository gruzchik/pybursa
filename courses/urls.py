from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import courses_list, courses_item


urlpatterns = patterns('',
    url(r'^$', courses_list),
    url(r'^(?P<course_id>\d+)/$', courses_item),
)
