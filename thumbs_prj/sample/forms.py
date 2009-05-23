#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms
from PIL import Image

class AttachmentForm(forms.Form):
    """Form for the attachment sample. Added a simple validation
    to accept only png files checking for 'image/png' in the
    content_type of the file"""
    image = forms.FileField(help_text="add a png or jpg file")
    comments = forms.CharField(widget= forms.Textarea, help_text="describe the image")

    def clean(self):
        "Validate the entire form"
        cleaned = self.cleaned_data        
        try:
            file = cleaned['image']
        except Exception, e:
            # perhaps this is not a file
            raise forms.ValidationError("Not valid file: %s" % e)
        if not file.content_type.lower() in ["image/jpeg", "image/png", "image/jpg"]:            
            raise forms.ValidationError("Just jpg or png files please")
        im = Image.open(file)
        if not im.format in ['JPEG','PNG']:
            raise forms.ValidationError("Just jpg or png files please")
        return cleaned


