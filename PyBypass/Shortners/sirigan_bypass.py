import requests
from base64 import b64decode


"""
https?://(safeurl\.sirigan\.my\.id\/)\S+
https://safeurl.sirigan.my.id/proses.html?asu=WVVoU01HTkViM1pNTWxZeFRHMDVlVnAzUFQwPQ=
"""

def sirigan_bypass(srigan_link:str) -> str:
    
    client = requests.Session()
    response = client.get(srigan_link)
    
    url = response.url.split('=', maxsplit=1)[-1]
    url = b64decode(url).decode('utf-8')

    while True:
        try: url = b64decode(url).decode('utf-8')
        except: break
    return url.split('url=')[-1]
   
   
