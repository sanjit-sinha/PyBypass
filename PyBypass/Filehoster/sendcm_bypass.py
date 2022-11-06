import requests 
import urllib.parse
import re
from bs4  import  BeautifulSoup


"""
https?://(send\.cm/)\S+
https://send.cm/ce3zr4cp0i7k
folder support isn't added yet.
"""


def sendcm_bypass(url:str) -> str:
    
    base_url = "https://send.cm/"
    client = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    
    response  = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    
    inputs = soup.find_all("input")
    file_id = inputs[1]["value"]
    file_name = re.findall("URL=(.*?) - ", response)[0].split("]")[1]
    parse = {"op": "download2", "id": file_id, "referer": url}
    
    resp = client.post(base_url, data=parse, headers=headers, allow_redirects=False)
    download_url = resp.headers["Location"]
    
    return download_url 
   
