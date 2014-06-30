from django.conf.urls import patterns
from sales.models import Customer
from sales import views
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ERP.views.home', name='home'),
    (r'^customer/new/$',views.CustomerCreateView.as_view()),
    (r'^customer/list/$', views.CustomerListView.as_view()),
    (r'^customer/update/(?P<pk>\d+)/$',views.CustomerUpdateView.as_view(model=Customer, template_name="Sales/Customer/Customer_Update.html")),
    (r'^customer/delete/(?P<pk>\d+)/$',DeleteView.as_view(model=Customer, template_name="Sales/Customer/Customer_Delete.html",
                                                             success_url="/customer/list/")),
    (r'^customer/(?P<pk>\d+)/$', DetailView.as_view(model=Customer, template_name="Sales/Customer/Customer_Display.html")),
    (r'^customer_process/$', views.Customer_Process),
)