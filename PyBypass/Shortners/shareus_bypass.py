import requests
import re


def shareus_bypassser(shareus_url: str) -> str:
	
	token = shareus_url.split("=")[-1]
	domain = "https://us-central1-my-apps-server.cloudfunctions.net/r?shortid="
		
	bypassed_url = domain+token
	response = requests.get(bypassed_url).text
	return response
	
