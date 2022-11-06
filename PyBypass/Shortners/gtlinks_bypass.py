import requests 
import time 
from bs4 import BeautifulSoup 



"""
https?://(gtlinks\.me\/)\S+
https?://(www\.theforyou\.in\/\?token=)\S+
https?://(loan\.kinemaster\.cc\/\?token=)\S+


https://gtlinks.me/j34BPkf
https://www.theforyou.in/?token=zrOFOaMK
https://loan.kinemaster.cc/?token=zrOFOaMK
"""

def gtlinks_bypass(url: str) -> str:
	
	url = url[:-1] if url[-1] == '/' else url
	
	if "theforyou.in" in url:
		token = url.split("=")[-1]
	else:
		url = requests.get(url).url
		token = url.split("=")[-1]
	

	domain = "https://go.theforyou.in/"

	
	client = requests.Session()
	response = client.get(domain+token, headers={"referer":domain+token})
	soup = BeautifulSoup(response.content, "html.parser")
	
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }
	

	time.sleep(5)
	headers={"x-requested-with": "XMLHttpRequest"}
	bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
	return bypassed_url
	
		
