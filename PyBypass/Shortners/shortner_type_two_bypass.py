from bs4 import BeautifulSoup 
import requests 
import time 
import re
 
 
 

shortner_dict =  {
     "https://droplink.co/": [
         "https?://(droplink\.co/)\S+",
         "https://droplink.co/",
         "https://yoshare.net",
         4
     ],
     "https://tnlink.in/": [
         "https?://(tnlink\.in\/)\S+",
         "https://gadgets.usanewstoday.club/",
         "https://usanewstoday.club/",
         9
     ],
     "https://ez4short.com/nzcU":[
         "https?://(ez4short\.com/)\S+",
         "https://ez4short.com/",
         "https://techmody.io/",
         5
     ],
     "https://xpshort.com/": [
         "https?://(xpshort\.com/)\S+",
         "https://push.bdnewsx.com/",
         "https://veganho.co/",
         10
      ],
      "http://vearnl.in/": [
          "http?://(vearnl\.in/)\S+",
          "https://go.urlearn.xyz/",
          "https://v.modmakers.xyz/",
          5
     ],
     "https://adrinolinks.in/":[
         "https?://(adrinolinks\.in/)\S+",
         "https://adrinolinks.in/",
         "https://wikitraveltips.com/",
         5
     ],
     "https://techymozo.com/": [
         "https?://(techymozo\.com/)\S+",
         "https://push.bdnewsx.com/",
         "https://veganho.co/",
         8
     ],
     "https://linkbnao.com/":[
         "https?://(linkbnao\.com/)\S+",
         "https://go.linkbnao.com/",
         "https://doibihar.org/",
         2
     ],
     "https://linksxyz.in/":[
         "https?://(linksxyz\.in/)\S+",
         "https://blogshangrila.com/insurance/",
         "https://cypherroot.com/",
         13
      ],
      "https://short-jambo.com/" :[
           "https?://(short\-jambo\.com/)\S+",
           "https://short-jambo.com/",
           "https://aghtas.com/how-to-create-a-forex-trading-plan/",
           10
     ],
     "https://ads.droplink.co.in/": [
         "https?://(ads\.droplink\.co\.in/)\S+",
         'https://go.droplink.co.in/',
         "https://go.droplink.co.in/",
         5
     ],
     "https://linkpays.in/": [
         "https?://(linkpays\.in/)\S+",
         "https://m.techpoints.xyz//",
         "https://www.filmypoints.in/",
         10
     ],
     "https://pi-l.ink/" : [
         "https?://(pi\-l\.ink/)\S+",
         "https://go.pilinks.net/",
         "https://poketoonworld.com/",
         5
      ],
      "https://link.tnlink.in/": [
          "https?://(link\.tnlink\.in/)\S+",
          "https://gadgets.usanewstoday.club/",
          "https://usanewstoday.club/",
          8
      ],
       "https://earn4link.in/": [
         "https?://(earn4link\.in/)\S+",
         "https://m.open2get.in/",
         "https://ezeviral.com/2022/03/01/why-is-cloud-hosting-the-ideal-solution/",
         3
     ],
     "https://open2get.in/": [
         "https?://(open2get\.in/)\S+",
         "https://m.open2get.in/",
         "https://ezeviral.com/2022/03/01/why-is-cloud-hosting-the-ideal-solution/",
         3
     ],
     
     
     
}  
 
def shortner_bypass(shortner_url:str, domain:str, referer:str, sleep_time:int) -> str:
    shortner_url = shortner_url[:-1] if shortner_url[-1] == '/' else shortner_url
    token = shortner_url.split("/")[-1]
 
    
    client = requests.Session()
    response = client.get(domain+token, headers={"referer": referer})
    
    soup = BeautifulSoup(response.content, "html.parser")   
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }
    
    time.sleep(sleep_time)
    headers={"x-requested-with": "XMLHttpRequest"}
    bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
    return bypassed_url 
        
 
def shortner_type_two_bypass(shortner_url: str) ->  str:
    
    for (key,value) in shortner_dict.items():
        if bool(re.match(FR"{value[0]}", shortner_url)): return shortner_bypass(shortner_url=shortner_url, domain=value[1], referer=value[2],sleep_time=value[3])
    return None 
    
    
