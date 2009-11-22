#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class Customer(models.Model):
    name    = models.CharField(max_length = 30, verbose_name=_('Nombre'))
    def __unicode__(self):
        return self.name


class CustomerForm(forms.ModelForm):
    #name  = forms.CharField(widget = forms.TextInput(attrs = {'size' : '15', }))
    class Meta:
        model = Customer
        exclude = ('id', )
