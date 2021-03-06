"""
Django settings for alboard2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sws%+0@5gy$pv^p7x2ej95)%!d@_6yecz8ssgorq=!1d-%d$55'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
COMPRESS_ENABLED = not DEBUG

ALLOWED_HOSTS = []

SITE_ID = 1



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'alboard2',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"



STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
MEDIA_URL = '/media/'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc --no-color {infile} {outfile}'),
)

BOWER_COMPONENTS_ROOT = BASE_DIR
BOWER_INSTALLED_APPS = (
    'tag-it#6ccd2de95e7cf7e254ad1a82e946450c21e40421',
    'jquery#2.1.3',
    'bootstrap#3.3.1',
    'jquery-pjax#1.9.4',
    'jquery-ui#1.11.2'
)



INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'grappelli',
    'reversion',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    
    'social.apps.django_app.default',
    
    'taggit',
    'markdown_deux',
    'sorl.thumbnail',
    'djangobower',
    'compressor',
    'easy_pjax',
    'crispy_forms',
    'widget_tweaks',
    'rosetta',
    'lockdown',
    'debug_toolbar',
    
    'booru',
    'alboard2',
    
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'lockdown.middleware.LockdownMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "booru.context_processors.context_processor",
    "alboard2.context_processors.context_processor",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'alboard2', 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'alboard2', 'static'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'alboard2', 'locale'),
)

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('sv', _("Swedish")),
    ('en', _("English")),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = 'alboard2.urls'
WSGI_APPLICATION = 'alboard2.wsgi.application'

GRAPPELLI_ADMIN_TITLE = "Alboard Admin"

DEBUG_TOOLBAR_CALLBACK = lambda req: DEBUG and not req.is_ajax()
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'alboard2.settings.DEBUG_TOOLBAR_CALLBACK',
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# 
# To enable password protection for your site, add to settings_local.py:
# 
# LOCKDOWN_URL_EXCEPTIONS = ()
# LOCKDOWN_PASSWORDS = ('mypass',)
# 
LOCKDOWN_URL_EXCEPTIONS = (
    r'.*',
)

try:
    from settings_local import *
except ImportError:
    pass
