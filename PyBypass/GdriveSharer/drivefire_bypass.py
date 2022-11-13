import requests
from urllib.parse import urlparse

"""
credits: Same Like https://github.com/xcscxr/hubdrive-dl/blob/main/hubdrive_dl.py

regex: https?://(drivefire)\S+

https://drivefire.co/file/1063238739

crypt_example: b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D

Note: 
If your 15 gb main drive get full then
It automatically get shifted to first TD in wich he have write access, so use drivefire_crypt of a account who have only one TD.
"""


def drivefire_bypass(url: str, drivefire_crypt: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)

    client = requests.Session()
    client.cookies.update({'crypt': drivefire_crypt})

    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"

    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'}, data={'id': url.split('/')[-1]}).json()['file']
        gd_id = res.rsplit("/", 1)[-1]
    except:
        return "Something went wrong. Could not generate GDrive URL for your Hubdrive Link"

    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link
