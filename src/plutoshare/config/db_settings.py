'''
Created on May 21, 2012

@author: greg
'''

import os

from tf_users.sharding import build_db_config, build_shard_config

def configure(presets):
    db_extras = {'OPTIONS': { 'init_command': 'SET storage_engine=INNODB'}}
    #db_extras = {'OPTIONS': { 'init_command': 'SET storage_engine=INNODB; SET foreign_key_checks = 0;'}}
    config_path = os.path.join(presets['PROJECT_ROOT'], 'spongebob', 'config')

    DATABASES = build_db_config(os.path.join(config_path, presets['DB_CONFIG_FILE']), extras=db_extras)
    SHARD_CONFIG = build_shard_config(os.path.join(config_path, presets['SHARD_CONFIG_FILE']))

    return locals()
