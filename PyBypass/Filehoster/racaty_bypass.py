import requests 
from bs4 import BeautifulSoup 


"""
https?://(racaty\.net/)\S+
https://racaty.net/10w86dphf8y2
https://racaty.io/10w86dphf8y2

"""

def racaty_bypass(url: str)-> str:
        
        
        
        client = requests.Session ()
        url= client.get(url).url
        
        url = url[:-1] if url[-1] == '/' else url
        token = url.split("/")[-1]
              
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
     
       

        if (btn := soup.find(class_="btn btn-dow")): return btn["href"]
        if (unique := soup.find(id="uniqueExpirylink")): return unique["href"]                                                         

