from django.conf.urls import patterns, url

from courses.views import CoursesListView, CoursesDetailView, CourseCreate, CourseUpdateView, CourseDelete


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', CoursesDetailView.as_view(), name="course_info"),
                       url(r'^$', CoursesListView.as_view(), name='courses_list'),
                       url(r'^add/$', CourseCreate.as_view(), name='course_add'), 
                       url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='course_edit'),
                       url(r'^delete/(?P<pk>\d+)/$', CourseDelete.as_view(), name='course_delete'),
                       )