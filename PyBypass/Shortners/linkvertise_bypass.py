import requests 

"""

https://linkvertise.com/417174/mommy/1
https?://(linkvertise\.com/)\S+
Linvertise subdomains = ["linkvertise.com", "linkvertise.net", "up-to-down.net", "link-to.net", "direct-link.net", "linkvertise.download", "file-link.net", "link-center.net", "link-target.net", "link-hub.net"]
"""

def linkvertise_bypass(url: str) -> str:
	
	linkvertise_bypass_api = "https://bypass.pm/bypass2?url="
	try: response = requests.get(linkvertise_bypass_api+url).json()["destination"]
	except: return None
	
	return response
	
	
