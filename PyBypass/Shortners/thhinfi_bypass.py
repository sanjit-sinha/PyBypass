import requests 
from bs4 import BeautifulSoup 

def thinfi_bypass(thinfi_url: str) -> str :
	response = requests.get(thinfi_url)
	soup = BeautifulSoup(response.content,  "html.parser").p.a.get("href")
	return soup
	
