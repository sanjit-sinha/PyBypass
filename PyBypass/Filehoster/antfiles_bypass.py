import requests 
from bs4 import BeautifulSoup 
from urllib.parse import urlparse


"""
https?://(antfiles\.com\/\?dl\=)\S+
https://antfiles.com/?dl=9dcf91d745f551a09845b3da580077a6
"""

def antfiles_bypass(antfiles_url: str)-> str:
    
    soup = BeautifulSoup(requests.get(antfiles_url).content, "html.parser")
    
    if (a := soup.find(class_="main-btn", href=True)): 
        final_url ="{0.scheme}://{0.netloc}/{1}".format(urlparse(antfiles_url), a["href"])
        return final_url
    return None

