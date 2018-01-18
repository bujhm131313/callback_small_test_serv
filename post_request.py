import requests
import json

data = {'some_date': 'lll'}
requests.get('http://18.195.186.70/callback_route', json=data)
