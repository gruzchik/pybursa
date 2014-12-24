from django.conf.urls import patterns, url

from coaches.views import CoachListView, CoachDetailView, CoachUpdateView, CoachCreate, CoachDelete


urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', CoachDetailView.as_view(), name="coach_info"),
                       url(r'^$', CoachListView.as_view(), name='coaches_list'),
                       url(r'^add/$', CoachCreate.as_view(), name='coach_add'),
                       url(r'^edit/(?P<pk>\d+)/$', CoachUpdateView.as_view(), name='coach_edit'),
                       url(r'^delete/(?P<pk>\d+)/$', CoachDelete.as_view(), name='coach_delete'),
                       )
