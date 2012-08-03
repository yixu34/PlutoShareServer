'''
Created on May 21, 2012

@author: greg
'''

import os

def configure(presets):
    ENABLE_SHARDING = True

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'tf_users.middleware.AuthenticationMiddleware',
    )

    ROOT_URLCONF = 'spongebob.urls'

    TEMPLATE_DIRS = (
        os.path.join(presets['PROJECT_ROOT'], 'templates')
    )

    INSTALLED_APPS = (
        'tf_util',
        'tf_users',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'south',
        'spongebob.front',
        'spongebob.farm',
        'spongebob.billing',
    )

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.
    TIME_ZONE = 'America/Los_Angeles'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale
    USE_L10N = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/"
    MEDIA_ROOT = os.path.join(presets['PROJECT_ROOT'], 'media')

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash if there is a path component (optional in other cases).
    # Examples: "http://media.lawrence.com", "http://example.com/media/"
    MEDIA_URL = '/m/'

    # URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
    # trailing slash.
    # Examples: "http://foo.com/media/", "/media/".
    ADMIN_MEDIA_PREFIX = '/media/'

    WHITELIST_ENABLED = False
    SOUTH_TESTS_MIGRATE = False

    # TODO: move this once we have the rest of these values. These are for dev
    FACEBOOK_APP_ID = '201572126607156'
    FACEBOOK_APP_SECRET = 'b56bb9c81b1a48a1c7c54a4306caa389'

    AUTH_EMAIL = False
    AUTH_FACEBOOK = True
    AUTH_GAMECENTER = True
    AUTHENTICATION_BACKENDS = []
    if AUTH_EMAIL:
        AUTHENTICATION_BACKENDS.append('tf_users.email.backend.EmailBackend')
    if AUTH_FACEBOOK:
        AUTHENTICATION_BACKENDS.append('tf_users.facebook.backend.FacebookBackend')
    if AUTH_GAMECENTER:
        AUTHENTICATION_BACKENDS.append('tf_users.game_center.backend.GameCenterBackend')
    TEST_UID = 5
    TEST_FACEBOOK_ID = '100002020647270'
    TEST_BACKEND = 'tf_users.facebook.backend.FacebookBackend'
    return locals()
