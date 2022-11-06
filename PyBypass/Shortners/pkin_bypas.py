import requests 
import time 
from bs4 import BeautifulSoup 

"""
https?://(pkin\.me/)\S+
https://pkin.me/U69JIgs
"""


def pkin_bypass(url: str) -> str:
	
	url = url[:-1] if url[-1] == '/' else url
	token = url.split("/")[-1]
	
	domain = "https://go.paisakamalo.in/"
	referer = "https://techkeshri.com/"
	token = url.split("/")[-1]
	user_agent= "Mozilla/5.0 (Linux; Android 11; 2201116PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	
	
	
	client = requests.Session()
	response = client.get(domain+token, headers={"referer": referer, "user-agent": user_agent})
	
	
	soup = BeautifulSoup(response.content, "html.parser")  
	
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	
	time.sleep(3)
	headers={"x-requested-with": "XMLHttpRequest", "user-agent": user_agent}
	bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
	return bypassed_url 
