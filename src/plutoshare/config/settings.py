'''
Created on May 21, 2012

@author: greg
'''

import importlib
import os
import sys

app_settings = {}

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
PARENT_DIR = os.path.basename(os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')))
BASE_DIR = os.path.basename(os.path.dirname(__file__))

PACKAGE = '%s.%s' % (PARENT_DIR, BASE_DIR)

app_settings['PROJECT_ROOT'] = PROJECT_ROOT

def configure_module(mod):
    try:
        m = importlib.import_module(mod, PACKAGE)
        module_settings = m.configure(app_settings)
        app_settings.update(module_settings)
    except ImportError as e:
        print e
        sys.exit(-1)

env_module = os.environ.get('DJANGO_ENV', 'env')

SETTINGS_MODULES = ['base', env_module, 'log_settings', 'email_settings', 'db_settings', 'cache_settings']

for module in ['.%s' % m for m in SETTINGS_MODULES]:
    configure_module(module)

globals().update(app_settings)
