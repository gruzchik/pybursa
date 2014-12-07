from django.views.generic import TemplateView
from pybursa import views

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
