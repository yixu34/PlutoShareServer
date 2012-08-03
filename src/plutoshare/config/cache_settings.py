'''
Created on May 21, 2012

@author: greg
'''

def configure(presets):
    num_replicas = 1 if len(presets['MEMCACHE_SERVERS']) > 1 else 0
    CACHES = {
        'default': {
            'BACKEND': 'tf_util.tf_memcache.TFMemcache',
            'LOCATION': presets['MEMCACHE_SERVERS'],
            'KEY_PREFIX': 'sb',
            'TIMEOUT': 60 * 60 * 24, # Cache for a day
            'OPTIONS': {
                'ketama': True,
                'num_replicas': num_replicas
            }
        }
    }

    return locals()
