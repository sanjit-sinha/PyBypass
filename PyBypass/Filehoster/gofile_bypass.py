import requests 



"""
https?://(gofile\.io\/d/)\S+
https://gofile.io/d/HZMNA4
"""

def gofile_bypass(url:str) -> str:
    
    api_uri = "https://api.gofile.io" 
    url = url[:-1] if url[-1] == '/' else url
    client = requests.Session()
    
    response  = client.get(f"{api_uri}/createAccount").json()
    
    data = {
        "contentId": url.split("/")[-1],
        "token": response ["data"]["token"],
        "websiteToken": 12345,
        "cache": "true",
    }
    response  = client.get(f"{api_uri}/getContent", params=data).json()
    
    for item in response["data"]["contents"].values():
        content = item
        download_url= content["link"]
       
        return download_url


