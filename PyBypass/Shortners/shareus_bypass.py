import requests
import re

"""
https?://(shareus\.in\/\?i=)\S+
https://shareus.in/?i=WbIeAA
"""

def shareus_bypass(shareus_url: str) -> str:
	
	token = shareus_url.split("=")[-1]
	domain = "https://us-central1-my-apps-server.cloudfunctions.net/r?shortid="
		
	bypassed_url = domain+token
	response = requests.get(bypassed_url).text
	return response
	
