import requests 

def tinyurl_bypass(tinyurl_url: str) -> str:
	response = requests.get(tinyurl_url).url
	return response
	
