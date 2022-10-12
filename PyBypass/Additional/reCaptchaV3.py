import re
import requests

"""
https://github.com/xcscxr/Recaptcha-v3-bypass
https?://(www\.google\.com\/recaptcha\/api2/)\S+
EXAMPLE OF ANCHOR_URL: https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8uaW86NDQz&hl=en&v=1B_yv3CBEV10KtI2HJ6eEXhJ&size=invisible&cb=4xnsug1vufyr
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

