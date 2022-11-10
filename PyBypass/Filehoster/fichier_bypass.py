import requests
from bs4 import BeautifulSoup


"""
['pjointe.com', 'dl4free.com', 'tenvoi.com', 'piecejointe.net', 'mesfichiers.org', 'desfichiers.com', 'megadl.fr', 'dfichiers.com', 'alterupload.com', 'cjoint.net', '1fichier.com']

https?://(pjointe|dl4free|tenvoi|piecejointe|mesfichiers|desfichiers|megadl|dfichiers|alterupload|cjoint|1fichier|\.com/\?)\S+

https://1fichier.com/?plpf4551k7lnlp411ujy
"""

def fichier_bypass(url:str) -> str:
	client = requests.Session()
	response = client.get(url)
	
	soup = BeautifulSoup(response.text, "html.parser")
	data = {"adz": soup.find("input").get("value")}
	
	
	rate_limit = soup.find("div", {"class": "ct_warn"})
	if "you must wait" in str(rate_limit).lower():
		try:
			numbers = [int(word) for word in str(rate_limit).split() if word.isdigit()]
			return f"1fichier.com is on limit for your ip. please wait {numbers[0]} min before trying again."
		except:
			return "1fichier.com is on limit for your ip. please wait few minutes/hour before trying again."

	else:
		r = client.post(url, json=data)
		soup = BeautifulSoup(r.text, "html.parser")
		download_url = soup.find(class_="ok btn-general btn-orange").get("href")
		return download_url 

		

