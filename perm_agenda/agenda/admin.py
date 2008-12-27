# -*- coding: UTF-8 -*-
"""Defines the Django admin manager representation for the
application."""

from django.contrib import admin
from models import Person

admin.site.register(Person)
