import requests 
import time 
from bs4 import BeautifulSoup 



def theforyou_bypass(theforyou_link: str) -> str:

	url = theforyou_link
	url = url[:-1] if url[-1] == '/' else url
	token = url.split("=")[-1]
	domain = "https://go.bloggertheme.xyz/"

	
	client = requests.Session()
	response = client.get(domain+token, headers={"referer":domain+token})
	soup = BeautifulSoup(response.content, "html.parser")
	
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	

	time.sleep(5)
	headers={"x-requested-with": "XMLHttpRequest"}
	bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
	return bypassed_url	
	
	
