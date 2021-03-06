#-*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404\.html$', TemplateView.as_view(template_name='404.html')),
        url(r'^500\.html$', TemplateView.as_view(template_name='500.html')),
    )
