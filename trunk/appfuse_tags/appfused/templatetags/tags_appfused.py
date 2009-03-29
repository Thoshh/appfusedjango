#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: General purpose tags for appfuse Django
#---------------------------------------------------------------------

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


def to_limit(value, arg):
    """Limits the number of characters of a string to the num
    passed as argument adding three dots
        Syntax: {{variable|to_limit:"number"}}

    where:
        variable is whatever wich has a string representation
        number: is the maximum lenght of the string
    """
    arg = int(arg)
    value=str(value)
    if arg < 4:
        raise template.TemplateSyntaxError, "argument must be bigger than 4 for the limit tag"
    if len(value) > arg:
        return "%s ..." % value[:arg-4]
    else:
        return value

register.filter('to_limit', to_limit)