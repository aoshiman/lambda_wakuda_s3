## -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import yaml
import lamvery

try:
    #  with open('config.yml') as f:
    with open(lamvery.secret.file('config.yml')) as f:
        _oauth_conf = yaml.load(f)

except Exception as e:
    print(e)

config = {
        'SEARCH_URL':  _oauth_conf['search_url'],
        'API_KEY': _oauth_conf['api_key'],
        'CUSTOM_SEARCH_ENGINE':  _oauth_conf['custom_search_engine'],
        'BUCKET': 'wakuda.aoshiman.org',
        'KEY': 'wakuda_image'
        }
