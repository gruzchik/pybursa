from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

from students.views import student_info, students_list, student_edit, student_add, student_delete


urlpatterns = patterns('',
                       url(r'^$', students_list, name='students_list'),
                       url(r'^(?P<student_id>\d+)/$', student_info,
                           name="student_info"),
                       url(r'^add/$', student_add, name='student_add'),
                       url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student_edit'),
                       url(r'^delete/(?P<student_id>\d+)/$', student_delete, name='student_delete'),
                       )
