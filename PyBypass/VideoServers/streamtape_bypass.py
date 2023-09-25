import requests
import re
import time

"""
Website : streamtape.com | streamtape.xyz | streamtape.to

Regex: https?://(streamtape\.(com|to|xyz)/)\S+

Example: https://streamtape.com/v/O1j7DBkmleiGwm/

Note: Bypassed url only open/download with the ip of machine you are working on
( for indian region  change the streamtape.com to streamtape.to)

"""

def streamtape_bypass( url:str)-> str:
    while True:
        response = requests.get(url)
        videolink = re.findall(r"document.*((?=id\=)[^\"']+)", response.text)
        nexturl = "https://streamtape.com/get_video?" + videolink[-1]
        if len(nexturl) > 50:
            return nexturl
        print("Incomplete URL, retrying in 2 seconds...")
        time.sleep(2)
