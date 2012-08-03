'''
Created on Apr 1, 2012

@author: greg
'''

# Django settings for SBServer project.
import os

def configure(presets):

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('Greg Soltis', 'greg@tinyfunstudios.com'),
    )

    MANAGERS = ADMINS

    DB_CONFIG_FILE = 'prod_db.cfg'
    SHARD_CONFIG_FILE = 'prod_shard.cfg'

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'xc0u18^g0!ac3k%0+2vgglmnr1)x^!o(n6@$m3t^(7l!(#kv!-'

    MEMCACHE_SERVERS = ['127.0.0.1:11211']

    LOG_DIR = '/var/log'
    LOG_FILENAME = os.path.join(LOG_DIR, 'spongebob.log')
    return locals()

