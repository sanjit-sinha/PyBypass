import requests
from bs4 import BeautifulSoup

"""
https?://(www\.upload\.ee/)\S+
https://www.upload.ee/files/14550364/908.txt.html
"""

def uploadee_bypass(url: str) -> str:
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    link = soup.find("a", attrs={"id": "d_l"})
    return link["href"]

