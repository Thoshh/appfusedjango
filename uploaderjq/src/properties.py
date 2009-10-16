#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
import os
debug=True
# managers

admins = (
        ('aaloy','aaloy@apsl.net'),
)

# Database configuration
database_engine='sqlite3'
database_name='db'
database_user=''
database_password=''
database_host=''
database_port=''
# Urls
app_root = os.path.dirname(os.path.realpath(__file__))
media_root=os.path.join(app_root, 'media/')
upload_folder=os.path.join(media_root, 'upload')
media_url = 'http://localhost:8000/media/'
admin_media_prefix ='/adm_media/'
# Cache and session backend
cache_backend = 'dummy:///'
cache_prefix='appfuse'
cache_seconds=300
session_engine='django.contrib.sessions.backends.cache'
secret_key='h61_=!)rbt%w=pwzzv$d3$ou9&m7^)=c#2ve)83l)ne)aowp5+'
language_code = 'es-es'
template_dirs = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(app_root,'templates/'),
)
