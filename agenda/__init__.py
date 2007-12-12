#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.djangosnippets.org/snippets/507/
# Author:forgems
# Posted:December 12, 2007

from django.template import loader
from django.conf import settings
from django.utils import translation
from django.utils.encoding import iri_to_uri
from django.utils  import cache 
import md5

template_cache = {} 
original_get_template = loader.get_template
def cached_get_template(template_name):
    global template_cache
    t = template_cache.get(template_name,None)
    if not t or settings.DEBUG:
        template_cache[template_name] = t = original_get_template(template_name)
    return t
loader.get_template = cached_get_template



def _generate_cache_key_i18n(request, headerlist, key_prefix):
    """Returns a cache key from the headers given in the header list.
    This function overrides the one that django provides in orde to consider
    the page language"""
    ctx = md5.new()
    lang = translation.get_language()
    for header in headerlist:
        value = request.META.get(header, None)
        if value is not None:
            ctx.update(value)
    return 'views.decorators.cache.cache_page.%s.%s.%s.%s' % (
               key_prefix, iri_to_uri(request.path), ctx.hexdigest(),lang)
cache._generate_cache_key=_generate_cache_key_i18n               



print "Inicializando agenda ..."