import requests

"""
https?://(mdisk\.me\/convertor)\S+
https://mdisk.me/convertor/53x30/vNv9FC
"""

def mdisk_bypass(url: str) -> str:
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = url[:-1] if url[-1] == '/' else url
    token = url.split("/")[-1]
    
    
    api = f"https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={token}"
    
    response = requests.get(api, headers=headers).json() 
        
    download_url = response["download"]
    download_url = download_url.replace(" ", "%20")
    
    return download_url
    
