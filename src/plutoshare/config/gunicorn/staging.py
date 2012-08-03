'''
Created on Mar 14, 2012

Staging config for gunicorn 
'''

bind = "127.0.0.1:9010"
workers = 3
daemon = True
logfile = '/var/log/sb_gunicorn.log'
loglevel = 'debug'
pidfile = '/var/run/sb_gunicorn_master.pid'
proc_name = 'sb'
