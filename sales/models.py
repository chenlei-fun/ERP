# -*- coding: utf-8 -*-
from django.db import models
from workflow.models import WorkflowActivity

from django.utils.translation import gettext as _


# Create your models here.
class Customer(models.Model):

    Name = models.CharField(max_length=50, verbose_name="姓名")
    Address = models.CharField(max_length=200, verbose_name="地址")
    Phone = models.CharField(max_length=10, verbose_name="电话")
    CellPhone = models.CharField(max_length=10, verbose_name="手机")
    QQ = models.CharField(max_length=10, verbose_name="QQ")
    CreateUser = models.CharField(max_length=10, verbose_name="创建人")
    CreateDate = models.DateField(verbose_name="创建日期" , auto_now= True)
    Activity = models.ForeignKey(
        WorkflowActivity,
        null=True,
        related_name='object',
        help_text=_('Related Object'))

    def __unicode__(self):
        return self.Name

    def get_absolute_url(self):
        return "/sales/distributor/list/"


class SalesOrder(models.Model):

    Customer = models.ForeignKey(Customer)
    CreateUser = models.CharField(max_length=10, verbose_name="创建人")
    CreateDate = models.DateField(verbose_name="创建日期", auto_now=True)


    def __unicode__(self):
        return self.id