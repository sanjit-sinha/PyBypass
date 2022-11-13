from bs4 import BeautifulSoup 
import requests 
import time 
import re
 
 
shortner_dict =  {
     "https://tekcrypt.in/tek/": [
         "https?://(tekcrypt\.in/tek/)\S+",
         "https://tekcrypt.in/tek/",
         20
     ],
     "https://link.short2url.in/": [
         "https?://(link\.short2url\.in/)\S+",
         "https://technemo.xyz/blog/",
         10
     ],
     "https://go.rocklinks.net/": [
         "https?://(go\.rocklinks\.net/)\S+",
         "https://dwnld.povathemes.com/",
         10
     ],
     "https://rocklinks.net/": [
         "https?://(rocklinks\.net/)\S+",
         "https://dwnld.povathemes.com/",
         10
     ],
     "https://earn.moneykamalo.com/": [
         "https?://(earn\.moneykamalo\.com/)\S+",
         "https://go.moneykamalo.com//",
         5
     ],
     "https://m.easysky.in/": [
         "https?://(m\.easysky\.in/)\S+",
         "https://techy.veganab.co/",
         5
     ],
     "https://indianshortner.in/": [
         "https?://(indianshortner\.in/)\S+",
         "https://indianshortner.com/",
         5
     ],
     "https://open.crazyblog.in/": [
         "https?://(open\.crazyblog\.in/)\S+",
         "https://hr.vikashmewada.com/",
         7
     ],
     "https://link.tnvalue.in/": [
         "https?://(link\.tnvalue\.in/)\S+",
         "https://internet.webhostingtips.club/",
         5
     ],
     "https://shortingly.me/": [
         "https?://(shortingly\.me/)\S+",
         "https://go.techyjeeshan.xyz/",
         5
     ],
     "https://dulink.in/": [
         "https?://(dulink\.in/)\S+",
         "https://tekcrypt.in/tek/",
         20
     ],
     "https://bindaaslinks.com/": [
          "https?://(bindaaslinks\.com/)\S+",
          "https://www.techishant.in/blog/",
           5
     ],
     "https://pdiskshortener.com/": [
         "https?://(pdiskshortener\.com/)\S+",
         "https://pdiskshortener.com/",
         10
      ],
      "https://mdiskshortner.link/": [
          "https?://(mdiskshortner\.link/)\S+",
          "https://mdiskshortner.link/",
          15
      ],
      "http://go.earnl.xyz/": [
          "https?://(go\.earnl\.xyz/)\S+",
          "https://v.earnl.xyz/",
          5
      ],
      "https://g.rewayatcafe.com/": [
           "https?://(g\.rewayatcafe\.com/)\S+",
           "https://course.rewayatcafe.com/",
           7
      ],
      "https://ser2.crazyblog.in/": [
          "https?://(ser2\.crazyblog\.in/)\S+",
          "https://ser3.crazyblog.in/",
          12
      ],
      "https://za.uy/" : [
           "https?://(za\.uy/)\S+",
           "https://za.uy/",
           5
      ],
      "https://bitshorten.com/": [
          "https?://(bitshorten\.com/)\S+",
          "https://bitshorten.com/",
          21
      ],
      "http://rocklink.in/":[
         "http?://(rocklink\.in/)\S+",
         "https://rocklink.in/",
         6
      ]
 
 }
 
def shortner_bypass(shortner_url:str, domain: str, sleep_time:int)-> str:
    
    shortner_url = shortner_url[:-1] if shortner_url[-1] == '/' else shortner_url
    token = shortner_url.split("/")[-1]
    
    client = requests.Session()
    response = client.get(domain+token, headers={"referer":domain+token})
    
    soup = BeautifulSoup(response.content, "html.parser")   
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }
    
 
    time.sleep(sleep_time)
    headers={"x-requested-with": "XMLHttpRequest"}
    bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
    return bypassed_url
    
 
def shortner_type_one_bypass(shortner_url: str) ->  str:
    for (key,value) in shortner_dict.items():
        if bool(re.match(FR"{value[0]}", shortner_url)): return shortner_bypass(shortner_url=shortner_url, domain=value[1], sleep_time=value[2])
    return None 
    
