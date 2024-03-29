# Django settings for crud project.
# -*- coding: UTF-8 -*-

# You have to customize your properties files. Just make a copy from
# properties.py.template and change the parameters to adapt them to your needs.
from properties import *

DEBUG = debug
TEMPLATE_DEBUG = debug
SITE_ROOT= site_root
MANAGERS = admins
APP_ROOT = app_root

DATABASE_ENGINE = database_engine               # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = database_name                   # Or path to database file if using sqlite3.
DATABASE_USER = database_user                   # Not used with sqlite3.
DATABASE_PASSWORD = database_password           # Not used with sqlite3.
DATABASE_HOST = database_host                   # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = database_port                   # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = media_root

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = media_url

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = admin_media_prefix

# Make this unique, and don't share it with anybody.
SECRET_KEY = secret_key

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#   'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APP_ROOT+'/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.admin',
    'filemanager',
)

if DEBUG:
    SESSION_EXPIRE_AT_BROWSER_CLOSE=True



ugettext = lambda s:s
LANGUAGES = (
    ('en', ugettext('English')),
    ('es', ugettext('Spanish')),
    ('ca', ugettext('Catalan')),
)


TEMPLATE_CONTEXT_PROCESSORS=("django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request")

ATTACHMENT_FOLDER= attachment_folder
ATTACHMENT_PATH = attachment_path

COPYRIGHT="apsl.net"
