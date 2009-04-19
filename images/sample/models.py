# -*- coding: UTF-8 -*-
__doc__ = """Defines de application model"""

from django.db import models

__author__="aaloy"
__date__ ="$19/04/2009 23:07:27$"


class Photo (models.Model):
    image = models.ImageField(upload_to='photos')
    comments = models.TextField()