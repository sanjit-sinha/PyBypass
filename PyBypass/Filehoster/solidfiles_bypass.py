import requests 
import json
import re


"""
https?://(www\.solidfiles\.com/v/)\S+
http://www.solidfiles.com/v/WqL3V2QjdmDZv
"""

def solidfiles_bypass(url: str) -> str:
    json_file = re.search(r"'viewerOptions\'\,\ (.*?)\)\;", requests.get(url).text)
    download_url = json.loads(json_file.group(1))["downloadUrl"]
    return download_url
   
    
