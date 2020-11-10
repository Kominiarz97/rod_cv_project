import requests
import json


def get_position():
    ip = requests.get('https://api.ipify.org').text
    send_url = f'http://api.ipstack.com/{ip}?access_key=0d2252b8ad943e2e9ff47e5574f3b2d2'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return lat, lon