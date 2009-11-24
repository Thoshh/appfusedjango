# Django settings for crud project.
# -*- coding: UTF-8 -*-

# You have to customize your properties files. Just make a copy from
# properties.py.template and change the parameters to adapt them to your needs.
import properties

DEBUG = getattr(properties,'debug', True)
TEMPLATE_DEBUG = DEBUG
SITE_ROOT=getattr(properties, 'site_root', "http://localhost:8000/")

MANAGERS =  getattr(properties, 'admins', list())

# NO default values here, you have to configure it yourself
DATABASE_ENGINE = properties.database_engine               # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = properties.database_name                   # Or path to database file if using sqlite3.
DATABASE_USER = properties.database_user                   # Not used with sqlite3.
DATABASE_PASSWORD = properties.database_password           # Not used with sqlite3.
DATABASE_HOST = properties.database_host                   # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = properties.database_port                   # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE =  getattr(properties,'time_zone','Europe/Madrid')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE =  getattr(properties,'language_code','es-es')

SITE_ID =  getattr(properties,'site_id',1)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT =  properties.media_root

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = properties.media_url

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = properties.admin_media_prefix

# Make this unique, and don't share it with anybody.
SECRET_KEY = properties.secret_key

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.CacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # Not using cache
)

ROOT_URLCONF = getattr(properties, 'root_urlconf', 'urls')

TEMPLATE_DIRS = getattr(properties, 'template_dirs', (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    r'templates/',
    )
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'agenda',
)
# set cache backend
CACHE_BACKEND=properties.cache_backend
CACHE_MIDDLEWARE_KEY_PREFIX=properties.cache_prefix
#CACHE_MIDDLEWARE_SECONDS=cache_seconds
# set session backed
#SESSION_BACKEND=session_backend

if DEBUG:
    SESSION_EXPIRE_AT_BROWSER_CLOSE=True

#Sesion engine if not default
#SESSION_ENGINE=session_engine    

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

COPYRIGHT="apsl.net"
