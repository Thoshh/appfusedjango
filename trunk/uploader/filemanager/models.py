#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.db import models
from django.conf import settings


class UserFile(models.Model):
    """Model which stores the files references uploaded by the users"""
    name = models.CharField(max_length=200, help_text="Name of the uploaded file")
    mime_type = models.CharField(max_length="100", blank=True)
    attachment = models.FileField(upload_to="attachments", blank=False,
                help_text="Your file goes here")
    created = models.DateTimeField(editable=False, auto_now_add=True, blank=False,
        db_index = True)

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, settings.ATTACHMENT_FOLDER, self.id)

    def get_download_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, settings.ATTACHMENT_FOLDER, self.name)


    def __unicode__(self):
        return self.attachment.name

