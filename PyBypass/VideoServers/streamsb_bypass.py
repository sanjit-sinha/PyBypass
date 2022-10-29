import requests
import random

"""
Website: streamsb.com ( have many domain )

domains = ['sbembed.com', 'sbembed1.com', 'sbplay.org', 'sbvideo.net', 'streamsb.net', 'sbplay.one', 'cloudemb.com', 'playersb.com', 'tubesb.com', 'sbplay1.com', 'embedsb.com', 'watchsb.com', 'sbplay2.com', 'japopav.tv', 'viewsb.com', 'sbplay2.xyz', 'sbfast.com', 'sbfull.com', 'javplaya.com', 'sbembed1.com', 'sbanh.com'] 

https?://(watchsb|streamsb)\.(com|net)\/\S+

https://sbanh.com/zsb9eanyxe1q.html
https://watchsb.com/e/ggyqfyu52zs2.html
https://sbplay2.xyz/e/v4yyijf2e2wa
https://sbembed.com/d/vi4xmgp1yhe4.html
https://streamsb.net/d/97vywgdww75r.html

"""

def streamsb_bypass(url: str):
	
	def rand_str():
		array = "abcdefghijklmnopqrstuvwqyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		return "".join([random.choice(array) for _ in range(12)])
		
	def hex_encode(string: str):
		return (string).encode("utf-8").hex()
		
	
	url = url[:-1] if url[-1] == '/' else url
		
	if ".html" in url : url_id= url.split("/")[-1].split(".")[-2]
	else: url_id = url.split("/")[-1]
	

	part_one = f"{rand_str()}||{url_id}||{rand_str()}||streamsb"
	final_url = f"https://watchsb.com/sources48/{hex_encode(part_one)}"
	headers={"watchsb":"sbstream", "referer":"url", "user-agent":"Mozilla/5.0 (Linux; Android 11; 2201116PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"}
	
	response = requests.get(final_url, headers=headers).json()["stream_data"]["file"]
	return response
	
	
	
	

