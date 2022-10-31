import requests 


"""
https?://(tinyurl.\com\/)\S+
https://tinyurl.com/2h3pttrc
"""

def tinyurl_bypass(tinyurl_url: str) -> str:
	response = requests.get(tinyurl_url).url
	return response
	
	
