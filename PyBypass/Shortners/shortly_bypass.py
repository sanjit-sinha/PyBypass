import requests 

"""
https://(www\.shortly\.xyz\/)\S+
https://www.shortly.xyz/r/e11c7b121cf59a162be977eff54e6d6e
"""

def shortly_bypass(shortly_url: str) -> str:
	
	shortly_url= shortly_url[:-1] if shortly_url[-1] == '/' else shortly_url
	token = shortly_url.split("/")[-1]

	shortly_bypass_api = "https://www.shortly.xyz/getlink.php/"
	response = requests.post(shortly_bypass_api, data={"id":token}, headers={"referer":"https://www.shortly.xyz/link"}).text
	
	return response
	
	
