#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: Admin configuration
#---------------------------------------------------------------------

__author__="aaloy"
__date__ ="$19/04/2009 23:07:39$"

from django.contrib import admin
from models import Photo


class PhotoManager(admin.ModelAdmin):
    "Ping model Admin"
    list_display = ('thumb', 'comments')

admin.site.register(Photo, PhotoManager)