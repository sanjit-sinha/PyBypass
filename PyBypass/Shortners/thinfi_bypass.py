import requests 
from bs4 import BeautifulSoup 


"""
https?://(thinfi\.com\/)\S+
https://thinfi.com/088ud
"""
def thinfi_bypass(thinfi_url: str) -> str :
	response = requests.get(thinfi_url)
	soup = BeautifulSoup(response.content,  "html.parser").p.a.get("href")
	return soup
	

	
