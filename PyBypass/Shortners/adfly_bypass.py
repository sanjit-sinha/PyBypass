import re
import requests
from base64 import b64decode
from urllib.parse import unquote

#https://github.com/xcscxr/adfly-bypass
#============================================================================================================

def decrypt_url(code):
    a, b = '', ''
    for i in range(0, len(code)):
        if i % 2 == 0: a += code[i]
        else: b = code[i] + b

    key = list(a + b)
    i = 0

    while i < len(key):
        if key[i].isdigit():
            for j in range(i+1,len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10: key[i] = str(u)
                    i = j					
                    break
        i+=1
    
    key = ''.join(key)
    decrypted = b64decode(key)[16:-16]

    return decrypted.decode('utf-8')

# ============================================================================================================

def adfly_bypass(url:str) -> str:
    res = requests.get(url).text
    
    out = {'error': False, 'src_url': url}
    
    try:
        ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        out['error'] = True
        return out
        
    url = decrypt_url(ysmm)

    if re.search(r'go\.php\?u\=', url):
        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
    elif '&dest=' in url:
        url = unquote(re.sub(r'(.*?)dest=', '', url))       
    out['bypassed_url'] = url
    
    return out['bypassed_url'] 
    
# ===========================================================================================================   
    
   

