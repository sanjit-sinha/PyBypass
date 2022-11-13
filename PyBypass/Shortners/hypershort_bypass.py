import re
import time
import requests 
from bs4 import BeautifulSoup

"""
https?://(hypershort\.com/)\S+
https://hypershort.com/XNKRIUPe
"""

def hypershort_bypass(hypershort_url:str):
	dom = "https://blog.miuiflash.com"

	client= requests.Session()
	
	response= client.get(hypershort_url)
	soup = BeautifulSoup(response.content, "html.parser")	
	
	token_response = client.get(f"{dom}/links/createToken.js").text
	token_regex = re.search("itsToken\.value = \S+", token_response)
	token = token_regex[0].split("=")[1].removesuffix('"').removeprefix(' "')

	
	inputs = soup.find(id="re-form").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }["getData"]
	
	next_page_link = soup.find("form").get("action")
	resp = client.post(next_page_link, data={"itsToken":token, "get2Data":data},
	headers={"referer":next_page_link})
	soup = BeautifulSoup(resp.content, "html.parser")	
	data = { input.get('name'): input.get('value') for input in inputs }
	
	time.sleep(4)
	tokenize_url = soup.find(name="iframe", id="anonIt").get("src")
	tokenize_url_resp = client.get(tokenize_url)
	soup = BeautifulSoup(tokenize_url_resp.content, "html.parser")	
	
	time.sleep(3)

	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	final_response = client.post(f"{dom}/blog/links/go", data=data, cookies= tokenize_url_resp.cookies, headers={"x-requested-with": "XMLHttpRequest", "referer":tokenize_url}).json()["url"]
	
	return final_response
	

