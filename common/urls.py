from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings
from django.contrib.auth.views import login, logout



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ERP.views.home', name='home'),
    (r'^login/$', 'common.views.login'),
    (r'^logout/$', logout),
)
