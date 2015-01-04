from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import contact


urlpatterns = patterns('',
                       url(r'^student/', include('students.urls')),
                       url(r'^coach/', include('coaches.urls')),
                       url(r'^course/', include('courses.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^contact/$', contact, name='contact_us'),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^$',
                           TemplateView.as_view(template_name='index.html'),
                           name='index'),
)
