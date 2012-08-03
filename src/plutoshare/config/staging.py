'''
Created on Apr 30, 2012

@author: yi
'''

import os

def configure(presets):

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('Greg Soltis', 'greg@tinyfunstudios.com'),
    )

    MEMCACHE_SERVERS = ['10.252.83.28:11211', '10.252.41.27:11211']

    SECRET_KEY = 'xc0u18^g0!ac3k%0+2vgglmnr1)x^!o(n6@$m3t^(7l!(#kv!-'

    LOG_DIR = '/var/log'
    LOG_FILENAME = os.path.join(LOG_DIR, 'spongebob.log')

    DB_CONFIG_FILE = 'staging_db.cfg'
    SHARD_CONFIG_FILE = 'staging_shard.cfg'
    return locals()

