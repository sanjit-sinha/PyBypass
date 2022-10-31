import requests 
import json
import re


"""
https?://(www\.solidfiles\.com/v/)\S+
http://www.solidfiles.com/v/WqL3V2QjdmDZv
"""

def solidfiles_bypass(solidfiles_url: str) -> str:
    
   json_file = re.search(r'viewerOptions\'\,\ (.*?)\)\;', requests.get(solidfiles_url).content)[1]
   return json.loads(json_file)["downloadUrl"]
    
   
