# -*- coding: UTF-8 -*-
__doc__ = """Defines de application model"""

from django.db import models
from imagekit.models import ImageModel

__author__="aaloy"
__date__ ="$19/04/2009 23:07:27$"

from django.db import models
from imagekit.specs import ImageSpec


class Photo (ImageModel):
    image = models.ImageField(upload_to='photos')
    comments = models.TextField()
    num_views = models.PositiveIntegerField(editable = False, default = 0)
    
    class IKOptions:
        spec_module = 'sample.specs'
        cache_dir = 'photos/cache'
        image_field = 'image'
        save_count_as = 'num_views'

    def thumb(self):
        if self.image:
            return '<img src="%s">' % self.thumbnail.url
        else:
            return ""
    thumb.allow_tags = True
    thumb.short_description = 'Foto'

