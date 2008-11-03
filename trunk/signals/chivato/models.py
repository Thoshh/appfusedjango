#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
import django.dispatch

class Eliminat(models.Model):
    user = models.CharField(max_length=30)
    created = models.DateTimeField(editable=False, auto_now_add=True, blank=False,
        db_index = True)

    def __unicode__(self):
        return self.user



def registra(sender, **kwargs):
    instancia = kwargs['instance']
    usuari = Eliminat(user=instancia.username)
    usuari.save()


pre_delete.connect(registra, sender=User)


class LogIp (models.Model):
    "Logs the ips and calling functions"
    name = models.CharField(max_length= 200)
    ip = models.IPAddressField()
    created = models.DateTimeField(editable=False, auto_now_add=True, blank=False,
        db_index = True)

in_view = django.dispatch.Signal(providing_args=['ip', 'name'])

def registra_ip(sender, **kwargs):
    ip = kwargs['ip']
    name = kwargs['name']
    log = LogIp(name= name, ip=ip)
    log.save()

in_view.connect(registra_ip)