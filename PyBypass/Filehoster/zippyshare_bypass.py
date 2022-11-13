import re
import requests 
import math
from bs4 import BeautifulSoup

"""
https?://www\d+\.zippyshare\.com/v/[^/]+/file\.html
https://www81.zippyshare.com/v/R5y49jcb/file.html
"""


def zippyshare_bypass(url:str)-> str:
	client = requests.Session()
	response = client.get(url)
	
	if (dlbutton := re.search(r'href = "([^"]+)" \+ \(([^)]+)\) \+ "([^"]+)', response.text)):
				folder, math_chall, filename = dlbutton.groups()
				math_chall = eval(math_chall)
				return "%s%s%s%s" % (re.search(r"https?://[^/]+", response.url).group(0), folder, math_chall, filename)
	           
	soup = BeautifulSoup(response, "html.parser")
	if (script := soup.find("script", text=re.compile("(?si)\s*var a = \d+;"))):
				sc = str(script)
				var = re.findall(r"var [ab] = (\d+)", sc)
				omg = re.findall(r"\.omg (!?=) [\"']([^\"']+)", sc)
				file = re.findall(r'"(/[^"]+)', sc)
	           
				if var and omg:
					a, b = var
					if eval(f"{omg[0][1]!r} {omg[1][0]} {omg[1][1]!r}") or 1: a = math.ceil(int(a) // 3)
					else: a = math.floor(int(a) // 3)
					divider = int(re.findall(f"(\d+)%b", sc)[0])
	               
	            
					return re.search(r"(^https://www\d+.zippyshare.com)", response.url).group(1) + \
                    "".join([file[0], str(a + (divider % int(b))), file[1]])
                    

