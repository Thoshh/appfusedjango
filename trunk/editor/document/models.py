#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.db import models


class Document (models.Model):
    "Defines a simple document"
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __unicode__(self):
        return self.title
