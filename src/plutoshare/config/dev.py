'''
Created on Apr 1, 2012

@author: greg
'''

#from spongebob.config.prod import *

import os

def configure(presets):

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        # ('Your Name', 'your_email@domain.com'),
    )
    MANAGERS = ADMINS

    # TODO: should probably change this at some point. Coordinate to make sure client isn't depending on it
    SECRET_KEY = 'xc0u18^g0!ac3k%0+2vgglmnr1)x^!o(n6@$m3t^(7l!(#kv!-'

    LOG_DIR = os.path.join(presets['PROJECT_ROOT'], 'logs')
    LOG_FILENAME = os.path.join(LOG_DIR, 'dev.log')

    DB_CONFIG_FILE = 'dev_db.cfg'
    SHARD_CONFIG_FILE = 'dev_shard.cfg'

    MEMCACHE_SERVERS = ['127.0.0.1:11211']

    return locals()


