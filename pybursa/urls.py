from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^index', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^list', TemplateView.as_view(template_name='list.html'), name='list'),
    url(r'^first', TemplateView.as_view(template_name='first.html'), name='student'),
    url(r'^admin/', include(admin.site.urls)),
)
