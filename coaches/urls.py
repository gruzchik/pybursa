from django.conf.urls import patterns, url

from coaches.views import coaches_list, coach_info, coach_add, coach_edit, coach_delete


urlpatterns = patterns('',
                       url(r'^(?P<coach_id>\d+)/$', coach_info,
                           name="coach_info"),
                       url(r'^$', coaches_list, name='coaches_list'),
                       url(r'^add/$', coach_add, name='coach_add'),
                       url(r'^edit/(?P<coach_id>\d+)/$', coach_edit, name='coach_edit'),
                       url(r'^delete/(?P<coach_id>\d+)/$', coach_delete, name='coach_delete'),
                       )
