#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _


class ConfirmForm(forms.Form):
    confirma = forms.BooleanField()

    def clean_confirma(self):
        valor = self.cleaned_data['confirma']
        if not valor:
            raise forms.ValidationError(_('Has de marcar el check box per confirmar que no hi vas!'))
        return valor

class InscripcioForm(ConfirmForm):
    comentario = forms.CharField(required = False, widget=forms.TextInput)
