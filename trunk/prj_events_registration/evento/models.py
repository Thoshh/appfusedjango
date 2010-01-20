# -*- coding: UTF-8 -*-
__doc__ = """Define el modelo para el evento"""

from django.db import models
from django.db.models import permalink
from django.contrib.admin.models import User
from datetime import date

class EventosActivosManager(models.Manager):
    def get_query_set(self):
        """Modifica el queryset para devolver sólo los eventos
        que están activos"""
        return super(EventosActivosManager, self).get_query_set().filter(activo = True). \
                filter(fecha__gt = date.today())


class Evento (models.Model):
    """Modelo para el evento. Un evento tiene una fecha de realización y 
    un número máximo de inscritos.    
    """
    slug = models.SlugField(max_length=30)
    nombre = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=200)
    descripcion_larga = models.TextField()
    fecha = models.DateField()
    lugar = models.TextField()
    capacidad = models.IntegerField(default = 20)
    activo = models.BooleanField(default=True)
    comments = models.TextField()

    # custom managers
    objects = models.Manager()
    activos = EventosActivosManager()

    @property
    def admite_inscripciones(self):
        "Devuelve verdadero si el evento admite inscripciones"
        return self.activo and (self.fecha > date.today())
    
    @property
    def inscritos(self):
        """Número de inscritos al evento"""
        return self.inscrito_set.all().count()

    def __unicode__(self):
        return u'%s %s' % (self.fecha, self.nombre)

    @permalink
    def get_absolute_url(self):
        """Absolute url lets you to define a unique url to identify the object.
        Is also used in the admin to implement the show at site (veure al lloc)
        feature, so it's worth to implement it. Decorator permalink makes to follow
        the DRY principle."""
        return ('ficha-evento',[self.slug,]) 

class Inscrito(models.Model):
    """Mantiene el registro de los inscritos a un evento"""
    user = models.ForeignKey(User)
    evento = models.ForeignKey(Evento)
    fecha_inscripcion = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-fecha_inscripcion']
