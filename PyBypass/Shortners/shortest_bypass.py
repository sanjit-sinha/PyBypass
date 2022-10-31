import re
import time
import requests
from urllib.parse import urlparse


"""
https://shorte.st/ 
http://festyy.com/eavTIP
https?://(shorte|festyy|gestyy|corneey|destyy|ceesty)\.(st|com)\/\S+

subdomains: [cllkme.com, festyy.com, gestyy.com, corneey.com, destyy.com, ceesty.com]
"""

def shortest_bypass(url: str) -> str:
  
    parsed_url = urlparse(url)
  
    client = requests.Session()
    resp = client.get(url, headers={'referer': url})
    session_id = re.findall('''sessionId(?:\s+)?:(?:\s+)?['|"](.*?)['|"]''', resp.text)[0]
    final_url = f"{parsed_url.scheme}://{parsed_url.netloc}/shortest-url/end-adsession"
    params = {
        'adSessionId': session_id,
        'callback': '_'
    }
    
    time.sleep(5)
    response = client.get(final_url, params=params, headers={'referer': url})
    dest_url = re.findall('"(.*?)"', response.text)[1].replace('\/','/')
    
    return dest_url


