import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


"""
https://github.com/xcscxr/Recaptcha-v3-bypass
https://github.com/xcscxr/ouo-bypass/blob/main/ouo-bypass.py

https?://(ouo\.(io|press)\/)\S+
https://ouo.io/EKrr4s
https://ouo.press/EKrr4s
"""

def RecaptchaV3(ANCHOR_URL):
    url_base = 'https://www.google.com/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = requests.Session()
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0]+'/'
    params = matches[1]
    res = client.get(url_base+'anchor', params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split('=') for pair in params.split('&'))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(url_base+'reload', params=f'k={params["k"]}', data=post_data)
    answer = re.findall(r'"rresp","(.*?)"', res.text)[0]    
    return answer

ANCHOR_URL = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8uaW86NDQz&hl=en&v=1B_yv3CBEV10KtI2HJ6eEXhJ&size=invisible&cb=4xnsug1vufyr'


def ouo_bypass(url: str):
    client = requests.Session()
    tempurl = url.replace("ouo.press", "ouo.io")
    p = urlparse(tempurl)
    id = tempurl.split('/')[-1]
    
    res = client.get(tempurl)
    next_url = f"{p.scheme}://{p.hostname}/go/{id}"

    for _ in range(2):
        if res.headers.get('Location'):
            break
            
        bs4 = BeautifulSoup(res.content, 'html.parser')
        inputs = bs4.form.findAll("input", {"name": re.compile(r"token$")})
        data = { input.get('name'): input.get('value') for input in inputs }
        
        ans = RecaptchaV3(ANCHOR_URL)
        data['x-token'] = ans        
        res = client.post(next_url, data=data, headers={'content-type': 'application/x-www-form-urlencoded'}, allow_redirects=False)
        next_url = f"{p.scheme}://{p.hostname}/xreallcygo/{id}"
    
    bypassed_link= str(res.headers.get("Location"))
    return bypassed_link


