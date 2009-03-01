#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: Forms definition
#---------------------------------------------------------------------

from django import forms
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.http import HttpResponse
try:
    from simplejson import JSONEncoder
except ImportError:
    try:
        from json import JSONEncoder
    except ImportError:
        from django.utils.simplejson import JSONEncoder


class ContactForm(forms.Form):
    "Defines the login for as in the Django sample"
    subject = forms.CharField(label="subject: *", max_length=100)
    message = forms.CharField(label="Request",
        widget=forms.Textarea(attrs={'rows':'10', 'cols':'80'}))
    email = forms.EmailField(label = "Your email *", max_length=120,
        error_messages = {'required': u"No e-mail, no message"})
    cc_myself = forms.BooleanField(required=False)

    def clean_message(self):
        "We wan't to verify that it containts some words"
        msg = self.cleaned_data['message'].strip()
        if len(msg.split(None))<5:
            raise forms.ValidationError(u"Really? This is quite short for a message")
        return msg


class LazyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj

def validate(request, form, new_url='', mimetype = "application/json"):
    """
        Returns a json structure with form errors validation
        valid: True if it has no validation errors
        url: is the url that we want to redirect
        errors: contanins the error structure
    """
    if form.is_valid():
        data = {
            'valid': True,
            'url': new_url
        }
    else:
        if request.POST.getlist('fields'):
            fields = request.POST.getlist('fields') + ['__all__']
            errors = dict([(key, val) for key, val in form.errors.iteritems() if key in fields])
        else:
            errors = form.errors
        final_errors = {}
        for key, val in errors.iteritems():
            if key == '__all__':
                final_errors['__all__'] = val
            if not isinstance(form.fields[key], forms.FileField):
                html_id = form.fields[key].widget.attrs.get('id') or form[key].auto_id
                html_id = form.fields[key].widget.id_for_label(html_id)
                final_errors[html_id] = val                
        data = {
            'valid': False,
            'url': new_url,
            'errors': final_errors,
        }
    json_serializer = LazyEncoder()
    return HttpResponse(json_serializer.encode(data), mimetype)
