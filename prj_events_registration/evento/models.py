# -*- coding: UTF-8 -*-
__doc__ = """Define el modelo para el evento"""

from django.core.mail import EmailMessage
from django.db import models
from django.db.models import permalink
from django.db.models.signals import post_delete
from django.contrib.admin.models import User
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


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

    @property
    def completo(self):
        """Un evento está completo si el número de inscritos supera la capacidad"""
        return self.inscrito_set.all().count() >= self.capacidad

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
    comentario = models.TextField(help_text = _("Comentari"), blank=True)
    en_lista_espera = models.BooleanField(default = False)
    class Meta:
        ordering = ['-fecha_inscripcion']

def llista_espera(sender, **kwargs):
    """Al borrar un evento comprobamos si hay gente en la lista de espera. En caso
    afirmativo el primero de la lista pasa a inscrito y se le envía un e-mail"""
    inscrito = kwargs['instance']
    if not inscrito.en_lista_espera and inscrito.evento.admite_inscripciones:
        try:
            primero = Inscrito.objects.filter(en_lista_espera = True, evento = inscrito.evento).order_by('id')[0]
            primero.en_lista_espera = False
            primero.save()
            subject = _("Enhorabona hi ha places per tu a l'event %s") % primero.evento.nombre
            from_email = settings.DEFAULT_FROM_EMAIL 
            texte = render_to_string('evento/no_en_lista.html', 
                                   {'inscripcion': primero, 'site': Site.objects.get_current()})
            msg = EmailMessage(subject, texte, from_email, [primero.user.email,])
            msg.content_subtype = "html"
            msg.send()
        except IndexError, e:
            # Vol dir que no hi ha gent en llista d'espera
            pass

post_delete.connect(llista_espera, sender=Inscrito)
