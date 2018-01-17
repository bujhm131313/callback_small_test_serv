import requests
import json

data = {'some_date': 'is_here'}
requests.post('http://127.0.0.1:5000/callback_route', json=data)
