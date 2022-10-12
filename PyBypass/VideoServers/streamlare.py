from bs4 import BeautifulSoup
import requests
import re


#-----------------------------------------------------------------------------------------------------------------------------------------------------
"""
Website: streamlare.com | sltube.org 

Example: https://sltube.org/v/0rZ45DrdRqmlM81R

Regex: https?://(streamlare|sltube\.(com|org)\/v/)\S+

Result: {'Original': {'label': 'Original', 'size': 3977525914, 'url': 'https://larecontent.com/download?token=SBFGQV8RCRFbR0dDQAlvHG8cREREHgcCRwQLAQYEHUBAXwNXHVBcXm8cX'}, 'headers': {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36'}}

Note: The direct download link will only work with  proper headers wich was is in the result dictionary.
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------


def streamlare_bypass(url:str)-> str:
	CONTENT_ID = re.compile(r"/[ve]/([^?#&/]+)")
	API_LINK = "https://sltube.org/api/video/download/get"
	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36"
	
	client = requests.Session()
	content_id = CONTENT_ID.search(url).group(1)

	r = client.get(url).text
	soup = BeautifulSoup(r, "html.parser")
	
	csrf_token = soup.find("meta", {"name":"csrf-token"}).get("content")
	xsrf_token =  client.cookies.get_dict()["XSRF-TOKEN"]
	headers={"x-requested-with": "XMLHttpRequest", "x-csrf-token": csrf_token, "x-xsrf-token":xsrf_token, 'referer': url, "user-agent":user_agent}
	payload = {"id": content_id}
         
	
	result = client.post(API_LINK, headers=headers, data=payload).json()["result"]
	result["headers"] = {"user-agent": user_agent} 
	return result
    
    
   
