#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy

from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django import forms
from models import UserFile


import os

class AttachmentForm(forms.Form):
    """Form for the attachment sample. Added a simple validation
    to accept only png files checking for 'image/png' in the
    content_type of the file"""
    attachment = forms.FileField(help_text="add a *.png file")

    def clean(self):
        "Validate the entire form"
        cleaned = self.cleaned_data
        try:
            file = cleaned['attachment']
        except Exception, e:
            # perhaps this is not a file
            raise forms.ValidationError("Not valid file: %s" % e)
        if file.content_type != "image/png":
            #TODO: check with PIL, just to be sure
            raise forms.ValidationError("Just png files please")
        return cleaned


def handle_uploaded_file(f):
    "Handles the upload file, writing it to the right location on disk"
    file_name = os.path.join(settings.ATTACHMENT_PATH, f.name)
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def attach(request):
    "Obtains the attachment and saves it to the disk"
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['attachment']
            record = UserFile(name = f.name,
                attachment = os.path.join(settings.ATTACHMENT_FOLDER, form.cleaned_data['attachment'].name),
                mime_type = f.content_type)
            handle_uploaded_file(f)
            record.save()
            return HttpResponseRedirect('/filemanager/list/')
    else:
        form = AttachmentForm()
    return render_to_response('attach.html', {'form':form},
            context_instance = RequestContext(request))

def list(request):
    "Lists the attached objects"
    attachments = UserFile.objects.all()
    return render_to_response('list.html', {'attachments':attachments})