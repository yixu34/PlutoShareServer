'''
Created on May 21, 2012

@author: greg
'''

import os

def configure(presets):
    LOG_MAXSIZE = 1024 * 1024 * 100
    LOG_BACKUPS = 7
    PURCHASE_LOG = 'purchase_log'
    ACTION_LOG = 'action_log'
    ACTION_LOG_FILENAME = os.path.join(presets['LOG_DIR'], 'action.log')
    PURCHASE_LOG_FILENAME = os.path.join(presets['LOG_DIR'], 'purchase.log')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)s %(message)s'
            }
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': presets['LOG_FILENAME'],
                'maxBytes': LOG_MAXSIZE,
                'backupCount': LOG_BACKUPS,
                'formatter': 'default'
            },
            ACTION_LOG: {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'd', # Rotate every day
                'interval': 1,
                'filename': ACTION_LOG_FILENAME,
                'backupCount': LOG_BACKUPS,
                'formatter': 'default'
            },
            PURCHASE_LOG: {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'd', # Rotate every day
                'interval': 1,
                'filename': PURCHASE_LOG_FILENAME,
                'backupCount': LOG_BACKUPS,
                'formatter': 'default'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            },
        },
        'loggers': {
            'spongebob': {
                'level': 'WARNING',
                'handlers': ['file'],
            },
            ACTION_LOG: {
                'level': 'INFO',
                'handlers': [ACTION_LOG],
            },
            PURCHASE_LOG: {
                'level': 'INFO',
                'handlers': [PURCHASE_LOG],
            },
        },
    }
    return locals()
