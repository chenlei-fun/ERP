# -*- coding: UTF-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from common.models import Module, SubModule
from sales.models import Customer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required,login_required
from workflow.models import Workflow, WorkflowActivity, Role,Participant, Transition

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "Sales/Customer/Customer_New.html"
    fields = ['Name','Address','Phone','CellPhone', 'QQ']

    def form_valid(self, form):
        form.instance.CreateUser = self.request.user
        wf = Workflow.objects.get(name='Distributor_Audit_Flow')
        wa = WorkflowActivity(workflow=wf, created_by=self.request.user)
        wa.save()

        wenyuan = Role.objects.get(name='文员')
        zhuguan = Role.objects.get(name = '主管')

        p1 = Participant(user=self.request.user, workflowactivity=wa)
        p1.save()

        wa.assign_role(self.request.user, self.request.user, wenyuan)
        wa.assign_role(self.request.user, self.request.user, zhuguan)

        wa.start(self.request.user)
        form.instance.Activity = wa
        return super(CustomerCreateView, self).form_valid(form)


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "Sales/Customer/Customer_Update.html"
    fields = ['Name','Address','Phone','CellPhone', 'QQ']


class CustomerListView( ListView ):
    model = Customer
    template_name = "Sales/Customer/Customer_List.html"
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        try:
            name = self.request.GET['name']
            phone = self.request.GET['phone']
            address = self.request.GET['address']
        except:
            name = ''
            phone = ''
            address = ''

        if (name != '' or phone != '' or address != ''):
            if( name != '' ):
                object_list = self.model.objects.filter(Name__icontains = name)
            if( phone != '' ):
                object_list = self.model.objects.filter(Phone__icontains = phone)
            if( address != '' ):
                object_list = self.model.objects.filter(Address__icontains = address)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CustomerListView, self).get_context_data(**kwargs)
        # Add in the publisher
        try:
            mid = self.request.GET['mid']
        except:
            mid = '1'
        modules = Module.objects.all().order_by("id")

        context['modules'] = modules
        return context


def Customer_Process(request):
    distributorid = request.GET['distributorid']
    transitionid = request.GET['transitionid']

    distributor = Customer.objects.get(id=distributorid)
    transition = Transition.objects.get(id=transitionid)

    distributor.Activity.progress(transition, request.user)

    return HttpResponseRedirect('/sales/customer/list/')

