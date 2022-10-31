import requests 
from bs4  import  BeautifulSoup


"""
https?://(sfile\.mobi/)\S+
https://sfile.mobi/1nNX2v3K5iI7
"""

def sfile_bypass(url:str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3239.83 Mobile Safari/537.36"
    }
    url = url[:-1] if url[-1] == '/' else url 
    token = url.split("/")[-1]

    soup = BeautifulSoup(requests.get("https://sfile.mobi/download/"+token, headers=headers).content, "html.parser") 
    
    download_url = soup.find("p").a.get("href")
    return download_url


