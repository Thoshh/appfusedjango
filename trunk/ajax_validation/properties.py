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
# logfile
logfile ='loggin.conf'
default_logger='apsl'

# Database configuration
database_engine='sqlite3'
database_name='db.sqlite'
database_user=''
database_password=''
database_host=''
database_port=''

# Paths and urls
app_root =  os.path.dirname(__file__)
media_root =  os.path.join(app_root, 'media/')
media_url = 'http://localhost:8000/media/'
admin_media_prefix ='/adm_media/'
template_dirs = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(app_root, 'templates/'),
)

# Cache and session backend
cache_backend = 'dummy:///'
cache_prefix='appfuse_ajax'
cache_seconds=300
session_engine='django.contrib.sessions.backends.cache'

# site configuration
secret_key='your-secret-key-goes-here'
language_code = 'es-es'
