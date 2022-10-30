import requests 

"""
Regex =  https?://(www\.mp4upload\.com/)\S+

Website: https://www.mp4upload.com/o62z8p1qqpwi

bypassed_result = {'bypassed_url': 'https://www6.mp4upload.com:282/d/sgxyzga5z3b4quuor2wbkzaslp3ksd66f3hohfvryptg4samc4pm7jvo/_opt_webapps_cron-download-upload_tmp_mp4upload_anime_127052.mp4', 'headers ': {'referer': 'https://mp4upload.com'}}

Note: To download from bypassed url you habe to give proper headers and set verify to False. Example->

requests.get("https://www6.mp4upload.com:282/d/sgxyzga5z3b4quuor2wbkzaslp3ksd66f3hohfvryptg4samc4pm7jvo/_opt_webapps_cron-download-upload_tmp_mp4upload_anime_127052.mp4", headers={'referer': 'https://mp4upload.com'},
verify=False) 
"""

def mp4upload_bypass(url):
	url = url[:-1] if url[-1] == '/' else url	
	headers = {'referer':'https://mp4upload.com'}
	token = url.split("/")[-1]		
		
	data =      {
	             'op': 'download2',
	             'id': token,
	             'rand': '','referer': 'https://www.mp4upload.com/',
	             'method_free': '','method_premium':''
	             }
	
	response = requests.post(url, headers=headers, data=data,allow_redirects=False)
	
	bypassed_json = {}
	bypassed_json["bypassed_url"] = response.headers["Location"]
	bypassed_json["headers "] = headers 
	return bypassed_json

