#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------
# Configuration for the uploader samples
# just adapt it to your own file folder structure
# -------------------------------------------------------------------
debug=True
# managers
admins = (
        ('aaloy','aaloy@apsl.net'),
)

# Database configuration
database_engine='sqlite3'
database_name='db.sqlite'
#in this example demo/demo
database_user=''
database_password=''
database_host=''
database_port=''
# Urls
app_root = r'/home/aaloy/workspace/appfusedjango/uploader'
media_root=app_root+r'/media/'
media_url = 'http://localhost:8000/media/'
admin_media_prefix ='/adm_media/'
site_root = 'http://localhost:8000/'

# Cache and session backend
cache_backend = 'dummy:///'
#cache_backend = 'locmem:///?timeout=50&max_entries=100'
#cache_backend= 'file:///tmp/appfuse_cache'
cache_prefix='appfuse_uploader'
cache_seconds=300
#session_engine='django.contrib.sessions.backends.cache'
secret_key='h61_=!)rbt%w=pwzzv$d3$ou9&m7^)=c#2ve)83l)ne)aowp5+'
attachment_folder='attachments'
attachment_path = media_root+attachment_folder

if __name__ == "__main__":
    pass
