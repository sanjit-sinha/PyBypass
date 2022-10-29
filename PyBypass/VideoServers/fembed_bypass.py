"""
fmed_list = ['fembed.net', 'fembed.com', 'femax20.com', 'fcdn.stream', 'feurl.com', 'layarkacaxxi.icu', 'naniplay.nanime.in', 'naniplay.nanime.biz', 'naniplay.com', 'mm9842.com', 'fembed-hd.com' ]

https?://(fembed|femax20|fcdn|feurl|naniplay|mm9842|layarkacaxxi|naniplay\.nanime|fembed\-hd)\.(com|net|stream|icu|in|biz)\S+

https://fembed-hd.com/v/246q0h26m5kj5ez

Note: Bypassed json file urls are restricted to ip of the device where script wws running. 

"""

import requests

def fembed_bypass(url: str) -> str:	

	url = url[:-1] if url[-1] == '/' else url
	
	TOKEN = url.split("/")[-1]	
	API = "https://fembed-hd.com/api/source/"
	
	response = requests.post(API+TOKEN).json()["data"]
	return response
	
	



