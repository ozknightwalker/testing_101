from __future__ import unicode_literals

import requests


def fetchAPI():
    response = requests.get('https://api.weibo.com/proxy/article/publish.json')
    json_response = response.json()
    if response.status_code == 200:
        return response.status_code, json_response
    return response.status_code, json_response
