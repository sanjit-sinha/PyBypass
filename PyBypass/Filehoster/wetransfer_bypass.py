import requests 
import re
import urllib.parse
from bs4  import  BeautifulSoup


"""
https?://(we\.tl/)\S+
https://we.tl/t-NsSDiMQNYF
www.wetransfer.py

"""


def wetransfer_bypass(url: str) -> str:
    
    if url.startswith("https://we.tl/"):
        r = requests.head(url, allow_redirects=True)
        url = r.url
    recipient_id = None
    params = urllib.parse.urlparse(url).path.split("/")[2:]
    
    if len(params) == 2:
        transfer_id, security_hash = params
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return None
        
    j = {
        "intent": "entire_transfer",
        "security_hash": security_hash,
    }
    
    if recipient_id:
        j["recipient_id"] = recipient_id
        
    s = requests.Session()
    r = s.get("https://wetransfer.com/")
    m = re.search('name="csrf-token" content="([^"]+)"', r.text)
    s.headers.update({"x-csrf-token": m[1], "x-requested-with": "XMLHttpRequest"})
    r = s.post(
        f"https://wetransfer.com/api/v4/transfers/{transfer_id}/download", json=j
    )
    j = r.json()
    dl_url = j["direct_link"]
 
    return dl_url
