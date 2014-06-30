# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Module(models.Model):
    Name = models.CharField(max_length=50, verbose_name="模块名")
    def __unicode__(self):
        return self.Name

    class Meta:
        ordering = ['Name',]

class SubModule(models.Model):
    Name = models.CharField(max_length=50, verbose_name="子模块名")
    Url = models.CharField(max_length=100)

    Module = models.ForeignKey(
        Module,
        null=False,
        related_name='SubModules',
        help_text="")

    def __unicode__(self):
        return self.Name

    class Meta:
        ordering = ['Name',]




