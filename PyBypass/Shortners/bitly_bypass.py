import requests 

def bitly_bypass(bitly_url: str) -> str:
	response = requests.get(bitly_url).url
	return response
	
