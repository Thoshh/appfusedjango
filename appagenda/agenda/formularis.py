#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# Definició dels formularis
# I like to define all the forms in one place and to avoid name clash
# i have maned the module formularis, that is forms in catalan, this is
# the nice part of having more than one mother language.
# -------------------------------------------------------------------
"""put your forms here"""

from django import forms
from agenda.models import Person

class PersonForm(forms.ModelForm):
    "Simple form for the Person model"
    class Meta:
        model = Person

class SearchForm(forms.Form):
    "Form for searching, no required fields"
    first_name = forms.CharField(max_length=30, required = False)
    last_name = forms.CharField(max_length=30, required = False)
    age = forms.IntegerField(required = False)


if __name__ == "__main__":
    pass
