import requests 


"""
https?://(uploadbaz\.me/)\S+
https://uploadbaz.me/tk3l8aygmwge
"""

def uploadbaz_bypass(url: str)-> str:
        
        url = url[:-1] if url[-1] == '/' else url
        token = url.split("/")[-1]
        
        client = requests.Session ()
        headers = {

            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        data = {
            'op': 'download2',
            'id': token,
            'rand': '',
            'referer': '',
            'method_free': '',
            'method_premium': '',

        }

        response = client.post(url, headers=headers, data=data, allow_redirects=False) 
        return response.headers["Location"]
        
        
