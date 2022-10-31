import requests 
import time 
from bs4 import BeautifulSoup 

"""
https?://(gplinks\.co/)\S+
https://gplinks.co/DDdozuB/
"""


def gplinks_bypass(url: str) -> str:
	
	url = url[:-1] if url[-1] == '/' else url
	token = url.split("/")[-1]
	
	domain ="https://gplinks.co/"
	referer = "https://mynewsmedia.co/"

	
	client = requests.Session()
	vid = client.get(url, allow_redirects= False).headers["Location"].split("=")[-1]
	url = f"{url}/?{vid}"

	response = client.get(url, allow_redirects=False)
	soup = BeautifulSoup(response.content, "html.parser")
	
	
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	

	time.sleep(5)
	headers={"x-requested-with": "XMLHttpRequest"}
	bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
	return bypassed_url	
	
	
