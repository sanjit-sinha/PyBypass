import re
import requests 
from bs4 import BeautifulSoup


"""
"https?://(sourceforge\.net/)\S+
https://sourceforge.net/projects/derpfestveux/files/DerpFest-13-Community-Tango-veux-20221004-2258.zip/download
"""

def sourceforge_bypass(url: str) -> str:
    link = re.findall(r"\bhttps?://sourceforge\.net\S+", url)[0]
    file_path = re.findall(r"files(.*)/download", link)[0]
    project = re.findall(r"projects?/(.*?)/files", link)[0]
    mirrors = (
        f"https://sourceforge.net/settings/mirror_choices?"
        f"projectname={project}&filename={file_path}"
    )
    page = BeautifulSoup(requests.get(mirrors).content, "html.parser")
    info = page.find("ul", {"id": "mirrorList"}).findAll("li")
    
    for mirror in info[1:]:
        link = f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}?viasf=1'
        return link
        
