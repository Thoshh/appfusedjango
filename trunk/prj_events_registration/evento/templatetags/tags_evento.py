#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import template
from evento.models import Inscrito, Evento
from django.contrib.auth.models import User

register = template.Library()

@register.tag('is_inscrito')
def do_is_inscrito_msg(parser, token):
    """Devuelve verdadero si el usuario se ha inscrito a un congreso y falso
    en caso contrario.    
    """
    bits = token.contents.split()
    if len(bits) == 5 and bits[3] =='as':
        return IsInscritoMsg(bits[1], bits[2], bits[4])
    else:
        return template.TemplateSyntaxError

class IsInscritoMsg(template.Node):
    """Comprubeba si un usuario está inscrito en el evento. 
    Por defecto si el usuario no está registrado le dirá que no está inscrito
    """

    def __init__(self, usuario, evento, context_variable):
        self.context_variable = context_variable
        self.usuario = template.Variable(usuario)
        self.evento = template.Variable(evento)

    def render(self, context):
        usuario = self.usuario.resolve(context)
        evento = self.evento.resolve(context)
        if usuario.is_anonymous:
            context[self.context_variable] = False
        else:
            context[self.context_variable] = Inscrito.objects.filter(user = usuario, evento = evento).count() > 0
        return ''
