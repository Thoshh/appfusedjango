#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# Definició dels formularis
# I like to define all the forms in one place and to avoid name clash
# i have maned the module formularis, that is forms in catalan, this is
# the nice part of having more than one mother language.
# -------------------------------------------------------------------
"""put your forms here"""

from django.forms import ModelForm
from agenda.models import Person

class PersonForm(ModelForm):
    "Simple form for the Person model"
    class Meta:
        model = Person


if __name__ == "__main__":
    pass
