from django.contrib import admin
from sales.models import Customer
from common.models import  Module, SubModule

class AdminDistributor(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Address', 'Phone')

class AdminModule(admin.ModelAdmin):
    list_display = ('id', 'Name')

class AdminSubModule(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Module')

# Register your models here.
admin.site.register(Customer, AdminDistributor)
admin.site.register(Module, AdminModule)
admin.site.register(SubModule, AdminSubModule)

