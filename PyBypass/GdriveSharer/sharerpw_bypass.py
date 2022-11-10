import re
import requests


'''
https?://(sharer\.pw\/file)\S+
https://sharer.pw/file/XuV3WQknRbB


NOTE: DO NOT use the logout button on website. Instead, clear the site cookies manually to log out.
If you use logout from website, cookies will become invalid.

Get your sharerpw_xsrf_token, sharerpw_laravel_session of sharer.pw from developer tools of your browser.
'''

def sharerpw_bypass(url: str, sharerpw_xsrf_token:None, sharerpw_laravel_session: None)-> str:
    
    client = requests.Session()
    client.cookies["XSRF-TOKEN"] = sharerpw_xsrf_token
    client.cookies["laravel_session"] = sharerpw_laravel_session
    
    
    res = client.get(url)
    token = re.findall("_token\s=\s'(.*?)'", res.text, re.DOTALL)[0]
    data = { '_token': token, 'nl' :1}

    try:
        response = client.post(url+'/dl', headers={ 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-requested-with': 'XMLHttpRequest'}, data=data ).json()
        drive_link = response
        return drive_link
    
    except:
        if drive_link["message"] == "OK": return "Something went wrong. Could not generate GDrive URL for your Sharer Link"
        else: return drive_link["message"]
    
  



