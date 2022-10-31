import requests 
from bs4 import BeautifulSoup 


"""
https?://(uppit\.com/)\S+
http://uppit.com/qmsn1wnk2g4l
"""

def uppit_bypass(url: str)-> str:
        
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

        response = client.post(url, headers=headers, data=data)
        soup = BeautifulSoup(response.text, "html.parser")  
     
        download_url= soup.find("span", {'style':'background:#f9f9f9;border:1px dotted #bbb;padding:7px;'}).a.get("href")
        
        return download_url 

                   
