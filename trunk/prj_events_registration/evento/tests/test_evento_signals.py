#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model
from django.conf import settings
import os
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from evento.models import *

class ListaEspera(TestCase):

    fixtures = [os.path.join(settings.APP_ROOT, "evento/fixtures/evento_testmaker.json"), ]

    def setUp(self):
        """Configuració inicial"""
        site = Site.objects.get(pk=1)
        site.domain = 'http://localhost:8000'
        site.name = 'localhost'
        site.save()
        # Asignamos un usuario en lista de espera
        usuario = User.objects.get(pk=3)
        evento = Evento.objects.get(pk=1)
        inscripcion = Inscrito(user = usuario, evento = evento, en_lista_espera=True)
        inscripcion.save()

    def test_lista_espera(self):
        """Comprueba que un usuario sale de la lista de espera al cancelar otro su
        inscripción a un evento"""
        usuario_inscrito = User.objects.get(pk=2)
        usuario_en_espera = User.objects.get(pk=3)
        evento = Evento.objects.get(pk=1)
        inscripcion_en_espera = Inscrito.objects.get(user=usuario_en_espera, evento = evento)
        self.assertEqual(inscripcion_en_espera.en_lista_espera, True)
        inscripcion = Inscrito.objects.get(user = usuario_inscrito, evento = evento)
        inscripcion.delete()
        inscripcion_en_espera = Inscrito.objects.get(user=usuario_en_espera, evento = evento)
        self.assertEqual(inscripcion_en_espera.en_lista_espera, False)

