#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('apps.{{ app_name }}.views',
    # url(r'^example_url/$', 'example_view', name='example'),
)
