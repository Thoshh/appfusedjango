#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model
from django.conf import settings
import os
from django.contrib.sites.models import Site

class CicloInscripcion(TestCase):

    fixtures = [os.path.join(settings.APP_ROOT, "evento/fixtures/evento_testmaker.json"), ]

    def setUp(self):
        """Configuració inicial"""
        site = Site.objects.get(pk=1)
        site.domain = 'http://localhost:8000'
        site.name = 'localhost'
        site.save()

    def test_index_not_logged(self):
        "Comprueba que vienen los dos eventos definidos"
        r = self.client.get('/', {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.context[-1]['eventos']), 2)
        self.assertEqual(unicode(r.context[-1]['params']), u'{}')

    def test_eventoinscribirsecreant_bits_amb_django_i_pytho(self):
        "Seleccionamos incripción a creant bits"
        r = self.client.get('/evento/inscribirse/creant-bits-amb-django-i-pytho/', {})
        #no estamos logueados, tiene que devolver un redirect
        self.assertEqual(r.status_code, 302)

    def test_accountslogin_get(self):
        r = self.client.get('/accounts/login/', {'next': '/evento/inscribirse/creant-bits-amb-django-i-pytho/', })
        self.assertEqual(r.status_code, 200)
        self.assertEqual(unicode(r.context[-1]['site_name']), u'localhost')
        self.assertEqual(unicode(r.context[-1]['site']), u'http://localhost:8000')
        self.assertEqual(unicode(r.context[-1]['form']), u"""<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="30" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>""")
        self.assertEqual(unicode(r.context[-1]['next']), u'/evento/inscribirse/creant-bits-amb-django-i-pytho/')
    
    def test_accountslogin(self):
        "Comprobamos el login"
        r = self.client.post('/accounts/login/', {'username': 'test', 'password': 'demo', 'next': '/evento/inscribirse/creant-bits-amb-django-i-pytho/', })

    def test_eventoinscribirsecreant_bits_amb_django_i_pytho(self):
        r = self.client.get('/evento/inscribirse/creant-bits-amb-django-i-pytho/', {})
        self.assertEqual(r.status_code, 302)

    def test_eventoinscribirsecreant_bits_amb_django_i_pytho(self):
        r = self.client.post('/evento/inscribirse/creant-bits-amb-django-i-pytho/', {'confirma': 'on', 'comentario': 'vull anar al creant bits', })
    
    def test_eventoinscripcion_realizadacreant_bits_amb_django_i_pytho(self):
        r = self.client.get('/evento/inscripcion-realizada/creant-bits-amb-django-i-pytho/', {})
        self.assertEqual(r.status_code, 302)
    
    def test_eventomis_inscripciones(self):
        r = self.client.get('/evento/mis-inscripciones/', {})
        self.assertEqual(r.status_code, 302)

    def test_eventocancelacreant_bits_amb_django_i_pytho_(self):
        r = self.client.get('/evento/cancela/creant-bits-amb-django-i-pytho/', {})
        self.assertEqual(r.status_code, 302)

    def test_eventocancelacreant_bits_amb_django_i_pytho(self):
        r = self.client.post('/evento/cancela/creant-bits-amb-django-i-pytho/', {'confirma': 'on', })

    def test_eventoinscripcion_canceladacreant_bits_amb_django_i_pytho(self):
        r = self.client.get('/evento/inscripcion-cancelada/creant-bits-amb-django-i-pytho/', {})
        self.assertEqual(r.status_code, 302)

    def test_accountslogout(self):
        r = self.client.get('/accounts/logout/', {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(unicode(r.context[-1]['title']), u'Logged out')

