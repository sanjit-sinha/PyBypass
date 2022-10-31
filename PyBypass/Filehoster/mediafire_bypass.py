from bs4 import BeautifulSoup 
import requests 
import re


"""
https://www.mediafire.com/download/8nqmnblivkv6tk2
https?://(www\.mediafire\.com\/download/)\S+
"""

def mediafire_bypass(mediafire_url: str) -> str:  
    link = re.search(r'\bhttps?://.*mediafire\.com\S+', mediafire_url)[0]
    page = BeautifulSoup(requests.get(link).content, 'html.parser')
    
    info = page.find('a', {'aria-label': 'Download file'}).get('href')
    return info
    
    
