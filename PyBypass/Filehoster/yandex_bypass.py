import requests 
import re

"""
https?://(yadi.sk|disk.yandex.com)\S+
https://disk.yandex.com/d/0PjgLth7S7o0Iw
"""
def yandex_bypass(url: str) -> str:
    api = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    return requests.get(api.format(url)).json()['href']
 
 
