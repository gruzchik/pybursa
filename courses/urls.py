from django.conf.urls import patterns, url

from courses.views import course_add, course_edit, course_delete#, courses_list, course_info
from courses.views import CoursesListView, CoursesView


urlpatterns = patterns('',
                       #url(r'^(?P<course_id>\d+)/$', course_info, name="course_info"),
		       url(r'^(?P<course_id>\d+)/$', CoursesView, name="course_info"),
                       #url(r'^$', courses_list, name='courses_list'),
                       url(r'^$', CoursesListView.as_view(), name='courses_list'),
                       url(r'^add/$', course_add, name='course_add'),
                       url(r'^edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
                       url(r'^delete/(?P<course_id>\d+)/$', course_delete, name='course_delete'),
                       )
