#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms

class ConfirmForm(forms.Form):
    confirma = forms.BooleanField()

    def clean_confirma(self):
        valor = self.cleaned_data['confirma']
        if not valor:
            raise forms.ValidationError('Has de marcar el check box per confirmar que no hi vas!')
        return valor

