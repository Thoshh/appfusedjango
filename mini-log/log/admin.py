# -*- coding: UTF-8 -*-
"""
Mòdul d'administració
"""
from django.contrib import admin
from models import Comment

admin.site.register(Comment)
