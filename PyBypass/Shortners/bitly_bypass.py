import requests 

"""
https?://(bit\.ly/)\S+
https://bit.ly/3gco4QU
"""

def bitly_bypass(bitly_url: str) -> str:
	response = requests.get(bitly_url).url
	return response
	
	
