import requests
from base64 import b64decode


def srigan_myid_bypass(srigan_link:str) -> str:
    
    client = requests.Session()
    response = client.get(srigan_link)
    
    url = response.url.split('=', maxsplit=1)[-1]

   while True:
        try: url = b64decode(url).decode('utf-8')
        except: break

   return url.split('url=')[-1]

