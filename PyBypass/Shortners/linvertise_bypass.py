import requests 


#Linvertise_domains = "linkvertise.com", "linkvertise.net", "up-to-down.net", "link-to.net", "direct-link.net", "linkvertise.download", "file-link.net", "link-center.net", "link-target.net", "link-hub.net"

def linvertise_bypass(linvertise_url: str) -> str:
	
	linvertise_bypass_api = "https://bypass.bot.nu/bypass2?url="
	try: response = requests.get(linvertise_bypass_api+linvertise_url).json()["destination"]
	except: return None
	
	return response
	
