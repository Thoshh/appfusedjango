#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
import os

# -----------------------------------------------------------------------------
# system configuration
# -----------------------------------------------------------------------------

debug=True
admins = (
        ('aaloy','aaloy@apsl.net'),
    )
manager = admins

# -----------------------------------------------------------------------------
# database configuration
# -----------------------------------------------------------------------------
database_engine='sqlite3'
database_name='db.sqlite'
database_user=''
database_password=''
database_host=''
database_port=''
# --------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# urls
# -----------------------------------------------------------------------------
app_root =  os.path.abspath(os.path.dirname(__file__))
media_root=os.path.join(app_root, 'media/')
media_url = 'http://localhost:8000/media/'
admin_media_prefix ='/adm_media/'
# ----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# cache and session
# -----------------------------------------------------------------------------
# use dummy if you don't want cache o while developing
# uses the default session engine (database, or file or memory)
cache_backend = 'locmem:///'
cache_prefix='appfuse'
cache_seconds=300
session_engine='django.contrib.sessions.backends.file'
#session_engine='django.contrib.sessions.backends.cache' #use cache if you have it
secret_key='no-oblidis-generar-la-secret-key'
# --------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# templates
# -----------------------------------------------------------------------------
language_code = 'en'
template_dirs = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(app_root,'templates/'),
)


# -----------------------------------------------------------------------------
# logging configuration
# -----------------------------------------------------------------------------
import logging
logging.basicConfig(
    #filename='the_filename_log_output.log',
    format="%(asctime)s-%(levelname)s-%(name)s-%(lineno)s-%(message)s",
    level = logging.INFO,
)
#logging.getLogger('app.module.file').setLevel(logging.INFO)
#logging.getLogger('app2.module.file').setLevel(logging.ERROR)
