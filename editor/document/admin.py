# -*- coding: UTF-8 -*-

from django.contrib import admin

__author__="aaloy"
__date__ ="$18/12/2008 18:59:54$"

from document.models import Document

class DocumentAdmin(admin.ModelAdmin):
    display_fields = ['title']
    class Media:
        js = ('/media/tiny_mce/tiny_mce.js',
              '/media/tiny_mce/textareas.js',)

admin.site.register(Document, DocumentAdmin)