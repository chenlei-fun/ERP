# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin

from sales import views
from common import views
import common.urls
import workflow.urls
import sales.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sales/', include(sales.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^common/', include(common.urls)),
    url(r'^workflow/', include(workflow.urls)),
    (r'^hello_pdf/$', views.hello_pdf),
    (r'^Test/$', TemplateView.as_view( template_name ='Test.html')),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_PATH}),

    #('^$', views.search_form),
    (r'^getPDF/$', views.getPDF),
)
