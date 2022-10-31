import re
import requests
from base64 import b64decode
from urllib.parse import unquote

"""
https://github.com/xcscxr/adfly-bypass
https://adf.ly/QtG5r
https?://(adf\.ly/)\S+

possible subdomains of adf.ly :-

["adf.ly", "j.gs", "q.gs", "ay.gy", "zo.ee", "babblecase.com", "riffhold.com", "microify.com", "pintient.com", "tinyium.com", "atominik.com", "bluenik.com", "bitigee.com", "atomcurve.com", "picocurl.com", "tinyical.com", "casualient.com", "battleate.com", "mmoity.com", "simizer.com", "dataurbia.com", "viahold.com", "coginator.com", "cogismith.com", "kaitect.com", "yoalizer.com", "kibuilder.com", "kimechanic.com", "quainator.com", "tinyium.com", "pintient.com", "quamiller.com", "yobuilder.com", "skamason.com", "twineer.com", "vializer.com", "viwright.com", "yabuilder.com", "yamechanic.com", "kializer.com", "yoineer.com", "skamaker.com", "yoitect.com", "activeation.com", "brisktopia.com", "queuecosm.bid", "nimbleinity.com", "rapidtory.com", "swiftation.com", "velocicosm.com", "zipteria.com", "zipvale.com", "agileurbia.com", "briskrange.com", "threadsphere.bid", "dashsphere.com", "fasttory.com", "rapidteria.com", "sprysphere.com", "swifttopia.com", "restorecosm.bid", "bullads.net", "velociterium.com", "zipansion.com", "activeterium.com", "clearload.bid", "brightvar.bid", "activetect.net", "swiftviz.net", "kudoflow.com", "infopade.com", "linkjaunt.com", "combostruct.com", "turboagram.com", "wirecellar.com", "streamvoyage.com", "metastead.com", "briskgram.net", "swarife.com", "baymaleti.net", "dapalan.com", "cinebo.net", "stratoplot.com", "thouth.net", "atabencot.net", "ecleneue.com", "twiriock.com", "uclaut.net", "linkup.pro", "lopoteam.com", "keistaru.com", "gloyah.net", "cesinthi.com", "sluppend.com", "fainbory.com", "infopade.com", "onisedeo.com", "ethobleo.com", "evassmat.com", "aclabink.com", "optitopt.com", "tonancos.com", "clesolea.com", "thacorag.com", "xterca.net", "larati.net", "cowner.net", "scuseami.net", "gatustox.net", "hinafinea.com", "fiaharam.net", "libittarc.com", "raboninco.com", "gdanstum.net", "aporasal.net", "motriael.com", "smeartha.com", "apticirl.com", "onizatop.net", "anthargo.com", "fumacrom.com", "regecish.net", "hurirk.net", "usfinf.net", "fumacrom.com", "xervoo.net", "usheethe.com", "eloism.net", "magybu.net", "uhishado.com", "hadsucma.com", "lyksoomu.com", "neexulro.net", "shycmedi.com", "chathu.apkmania.co", "alien.apkmania.co", "adf.acb.im", "packs.redmusic.pl", "packs2.redmusic.pl", "dl.android-zone.org", "out.unionfansub.com", "sostieni.ilwebmaster21.com", "fuyukai-desu.garuda-raws.net", "st.uploadit.host", "vonasort.com", "atharori.net", "hideadew.com", "favoacew.com", "barsoocm.com", "chuxoast.com" ]
"""

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
    
