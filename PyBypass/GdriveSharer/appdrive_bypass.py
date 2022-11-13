import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


"""
Appdrive Domain: appdrive.info

Appdrive Look Alike Domain: "driveapp.in", "drivehub.in" , "gdflix.pro", "drivesharer.in", "drivebit.in", "drivelinks.in", "driveace.in", "drivepro.in", "gdflix.top"


Note:- Each Domain require login email and password. You have to login all website separately to bypass that website link
( Tip use same email to login all website and go to  dashboard and create same password of all domain )


Parameters: 
appdrive_email and appdrive_password params should be of website not GOOGLE ACCOUNT
you can configure custom drive_id and folder_id from dashboard to save file in that destination.

Note: Some appdrive links don't need authorization ( email, password) like :( ex:  https://appdrive.info/file/m6p1PbFF49aqb4MOHrz1 ) , whereas some need authorization ( ex: https://appdrive.info/file/78owWyzsKPRuU5QB2VyG)

Regex: 
https?://(anidrive|driveroot|driveflix|indidrive|drivehub|appdrive|driveapp|driveace|gdflix|drivelinks|drivebit|drivesharer|drivepro)\.\S+

Domains Examples:
https://appdrive.info/file/78owWyzsKPRuU5QB2VyG
https://gdflix.top/file/8orswDGb6i
https://gdflix.pro/file/24pEEKH1Vp


appdrive_bypass("https://appdrive.info/file/m6p1PbFF49aqb4MOHrz1", appdrive_email="xyz@gmail.com", appdrive_password="appdrive")

"""


def account_login(client, url, appdrive_email, appdrive_password):
    data = {
        'email': appdrive_email,
        'password': appdrive_password
    }
    client.post(f'https://{urlparse(url).netloc}/login', data=data)

 
    
def gen_payload(data, boundary=f'{"-"*6}_'):
    data_string = ''
    
    for item in data:
        data_string += f'{boundary}\r\n'
        data_string += f'Content-Disposition: form-data; name="{item}"\r\n\r\n{data[item]}\r\n'
        
    data_string += f'{boundary}--\r\n'
    return data_string



def appdrive_lookalike(client, drive_link):
    try:
        response = client.get(drive_link).text
        soup = BeautifulSoup(response, "html.parser")
        new_drive_link = soup.find(class_="btn").get("href")
        return new_drive_link
    except: return drive_link

			
def appdrive_bypass(url: str, appdrive_email=None, appdrive_password=None) -> str:

    client = requests.Session()
    client.headers.update({
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    })
    
    url = client.get(url).url 
    response = client.get(url)   
    try:
        key = re.findall('"key",\s+"(.*?)"', response.text)[0]
        soup = BeautifulSoup(response.text,  "html.parser")
        ddl_btn = soup.find(id="drc")
    except:
        return "Something went wrong. Could not generate GDrive URL for your Given Link"
    
    headers = { "Content-Type": f"multipart/form-data; boundary={'-'*4}_"} 
    data = { 'type': 1,  'key': key, 'action': 'original'}
    
    if ddl_btn != None:  data['action'] = 'direct'
    else : account_login(client, url, appdrive_email, appdrive_password)
    	 
  
        
    while data['type'] <= 3:
        try:  response = client.post(url, data=gen_payload(data), headers=headers).json() ;  break 
        except: data['type'] += 1   
 
        
    if 'url' in response:
        drive_link = response["url"]
        if urlparse(url).netloc in ("driveapp.in", "drivehub.in" , "gdflix.pro", "drivesharer.in", "drivebit.in", "drivelinks.in", "driveace.in", "drivepro.in", "gdflix.top"): return appdrive_lookalike(client,  drive_link)
        else : return drive_link
    		     	 	
    elif  'error' in response and response['error']: return response['message']
    else: return "Something went wrong. Could not generate GDrive URL for your Given Link"
    



