import requests
from bs4 import BeautifulSoup


"""
https?://(krakenfiles\.com\/view/)\S+
https://krakenfiles.com/view/JEp6lUTRUW/file.html
"""
def krakenfiles_bypass(url:str)-> str:
    
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    token = soup.find("input", id="dl-token")["value"]
    hashes = [
        item["data-file-hash"]
        for item in soup.find_all("div", attrs={"data-file-hash": True})
    ]
    if not hashes:
        return None 
        
    dl_hash = hashes[0]
    payload = f'------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="token"\r\n\r\n{token}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    
    headers = {
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        "cache-control": "no-cache",
        "hash": dl_hash,
    }
    
    dl_link_resp = requests.session().post(
        f"https://krakenfiles.com/download/{hash}", data=payload, headers=headers
    )
    dl_link_json = dl_link_resp.json()
    download_url  = dl_link_json["url"]
    download_url  = download_url .replace(" ", "%20")
    return download_url 
    
      
