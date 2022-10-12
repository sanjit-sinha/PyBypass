import time
import requests
from bs4 import BeautifulSoup 
import cloudscraper 
import re

DOODSTREAM = "https://dood.la/"

PASS_MD5_RE = re.compile(r"/(pass_md5/.+?)'")
TOKEN_RE = re.compile(r"\?token=([^&]+)")


def extract(session, url):
    response = session.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97"})
    
    #print(response.text)
    soup = BeautifulSoup(response.text,  "html.parser")
    #rint(soup)
    ok = soup.find(class_="btn btn-primary d-flex align-items-center justify-content-between")
    
    if not response.status_code < 400:
        return []

    embed_page = session.get(url).text
    has_md5 = PASS_MD5_RE.search(embed_page)
    print(has_md5)

    if not has_md5:
        return []

    has_token = TOKEN_RE.search(embed_page)
    if not has_token:
        return []

    return [
        {
            "stream_url": "{}doodstream?token={}&expiry={}".format(
                session.get(
                    DOODSTREAM + has_md5.group(1), headers={"referer": DOODSTREAM}
                ).text,
                has_token.group(1),
                int(time.time() * 1000),
            ),
            "headers": {"referer": DOODSTREAM},
        }

    
            ]
session = cloudscraper.create_scraper(allow_brotli=False) 
print(extract(session, "https://dood.la/e/478jzg7v4kv6"))            



#[Program finished]
<re.Match object; span=(12376, 12471), match="/pass_md5/52149069-197-45-1665607060-750c78d46861>
[{'stream_url': 'https://ki517mi.dood.video/u5kjumgvcpg3sdgge64ewiy7dsmnrazjrqaov7lbyxfz7svfteqenqrze4wa/naohcubfx3~doodstream?token=80i2f9z2hoh5zzehg1546rsb&expiry=1665607061122', 'headers': {'referer': 'https://dood.la/'}}]

[Program finished]
