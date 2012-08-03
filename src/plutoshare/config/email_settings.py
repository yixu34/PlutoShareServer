'''
Created on May 21, 2012

@author: greg
'''

def configure(presets):
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'bobthebuilder@tinyfunstudios.com'
    EMAIL_HOST_PASSWORD = '2thecloud!'
    EMAIL_PORT = 587
    return locals()
