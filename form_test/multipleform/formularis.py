#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: Forms definition
#---------------------------------------------------------------------
__author__="aaloy"
__date__ ="$23/11/2008 18:17:14$"

from django import forms

class ContactForm(forms.Form):
    "Defines the login for as in the Django sample"
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class LoginForm(forms.Form):
    user = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10, widget= forms.PasswordInput)

class InfoForm(forms.Form):
    user = forms.CharField(max_length=10)
    message = forms.CharField()