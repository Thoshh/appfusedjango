# -*- coding: UTF-8 -*-
__doc__ = """Defines de application model"""

from django.db import models
from django.db.models import permalink

class Person (models.Model):
    """"Defines the model for the person entity.
    This is a minimum test model.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    comments = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @permalink
    def get_absolute_url(self):
        """Absolute url lets you to define a unique url to identify the object.
        Is also used in the admin to implement the show at site (veure al lloc)
        feature, so it's worth to implement it. Decorator permalink makes to follow
        the DRY principle."""
        return ('agenda-ficha',['editar',self.id]) 

