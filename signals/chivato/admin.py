# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import Eliminat, LogIp

class EliminatAdmin(admin.ModelAdmin):
    list_display = ('created','user')
    list_filter = ('created',)
    search_fields = ['user',]

class LogIpAdmin(admin.ModelAdmin):
    list_display= ('ip','name')


admin.site.register(Eliminat, EliminatAdmin)
admin.site.register(LogIp, LogIpAdmin)