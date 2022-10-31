from bs4 import BeautifulSoup 
import requests 

"""
https://anonfiles.com/32j4A56dyd
https?://(anonfiles\.com)\S+
"""

def anonfiles_bypass(anonfiles_url: str) -> str:
    soup = BeautifulSoup(requests.get(anonfiles_url).content, "html.parser")
    if (dlurl := soup.find(id="download-url")): return dlurl["href"]
    
 
