
<div align="center">
 <h1>A python library to bypass links</h1>
<img src="https://telegra.ph/file/d83e9d64160666fec7ad6.png" align="center" style="width: 100%" />
</div>

------
**Note: New and Stable Version of this library is available. Please upgrade it by command**
```
python -m pip install --upgrade PyBypass
```
**You can read the Changelogs [here](https://github.com/sanjit-sinha/PyBypass/blob/main/CHANGELOGS.md)**
_____

<div align="center">
<h1><b>PyBypass</b></h1>
</div>

PyBasser is a python library wich can bypass various type of links and give you direct access to the content of the link without getting bothered by annoying ads websites redirection.

Currently it can bypass various types of shortlinks, filehosters, videoservers and gdrive sharer links.

you can also find PyBypass n pypi.org https://pypi.org/project/PyBypass/

-----

<div align="center">
<h1><b>Supported website links</b></h1>
</div>

#### Shortners

> try2link.com, adf.ly, bit.ly, ouo.io, ouo.press, shareus.in, shortly.xyz, tinyurl.com, thinfi.com, hypershort.com ,safeurl.sirigan.my.id, gtlinks.me, loan.kinemaster.cc, theforyou.in, linkvertise.com, shorte.st, earn4link.in, tekcrypt.in, link.short2url.in, go.rocklinks.net, rocklinks.net, earn.moneykamalo.com, m.easysky.in, indianshortner.in, open.crazyblog.in, link.tnvalue.in, shortingly.me, open2get.in, dulink.in, bindaaslinks.com, za.uy, pdiskshortener.com, mdiskshortner.link, go.earnl.xyz, g.rewayatcafe.com, ser2.crazyblog.in, bitshorten.com, rocklink.in, droplink.co, tnlink.in, ez4short.com, xpshort.com, vearnl.in, adrinolinks.in, techymozo.com, linkbnao.com, linksxyz.in, short-jambo.com, ads.droplink.co.in, linkpays.in, pi-l.ink, link.tnlink.in , pkin.me

### Filehoster

> nonfiles.com, antfiles.com, 1fichier.com, gofile.io, hxfile.co, krakenfiles.com, mdisk.me, mediafire.com, pixeldrain.com, racaty.net, send.cm, sfile.mobi, solidfiles.com, sourceforge.net, uploadbaz.me, upload.ee, uppit.com, userscloud.com, we.tl, disk.yandex.com, zippyshare.com, wetransfer.com


### Gdrivesharer

> appdrive.info, new2.gdtot.sbs, hubdrive.me, sharer.pw
( appdrive lookalike dmains: driveapp.in, drivehub.in, gdflix.pro, drivesharer.in, drivebit.in, drivelinks.in, driveace.in, drivepro.in, gdflix.top )


### VideoServers
> fembed-hd.com, mp4upload.com, sltube.org, watchsb.com, streamtape.com
 
------ 

<div align="center">
<h1><b>Installation Guide and How to use?</b></h1>
</div>

**Installation**
```bash
 python -m pip install PyBypass
```
**Updating Library**
```bash
python -m pip install --upgrade PyBypass
```

------

<div align="center">
<h1><b>How to use?</b></h1>
</div>

- PyBypass is an library wich mean you can import it into your own code and use it accordingly.

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://www40.zippyshare.com/v/DkywSXEu/file.html")

print(bypassed_link)
```

- some website have so many subdomains so it is hard to auto detect every link. use parameter `name` to bypass those type of links.
- ( some common website like those are adfly, linkvertise, short.st, appdrive etc. )
- you can find the list on `name` parameter wich can be used for diferent websites [here](https://katb.in/abefuqetoxe)

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://link-center.net/209924/ofbulk", name="linkvertise")

```


- To bypass gdrivesharer links you have to provide some parameters wich are required to bypass the link.

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://new2.gdtot.sbs/file/105111102182", gdtot_crypt="b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D")

```
<details>
<summary><strong>To know more about parameters click here.</strong></summary>
<ul>
<br>
	<li><b>GDTOT parameters.</b><br><br>
	GDTOT links take required parameter <b>gdtot_crypt</b> to bypass the gdtot links.<br><br>
	You can find Your gdtot_crypt by login in gdtot account > open developer mode > go to cookies > copy crypt value.<br><br>
	Always use a new google account for doing this. keep only one TD in that drive because after reaching 15gb limit Gdtot, Hubdrive, sharer.pw will copy the file in the  first TD in wich you have write access.
	</li>
<br>
    <li><b>APPDRIVE parameters. </b><br><br>
    Appdrive and it's lookalike domains take required parameters <b>appdrive_email </b> and <b>appdrive_password</b><br><br>
    appdrive_email and appdrive_password params should be of website not GOOGLE ACCOUNT.
You can also configure custom drive_id and folder_id from dashboard to save file in that destination.<br><br>
     Each appdrive lookalike Domain require login email and password. You have to login in all website separately to bypass that website link.
( Tip use same email to login all website and go to  dashboard and create same password of all domain )</li>
<br>
	<li><b>HUBDRIVE parameters.</b><br><br>
	Hubdrive links  take required parameter <b>hubdrive_crypt</b> to bypass the hubdrive links.
	</li>
<br>
   <li><b>Sharer.pw parameters.</b><br><br>
	sharer.pw links  take required parameter <b>sharerpw_xsrf_token</b> and <b> sharerpw_larvel_token</b>  to bypass the  sharer.pw links. You can find these parameters in developer tool of browser after logging in with your google account. 
	</li>
    
</ul>
</details>

- You can add try and catch exceptions while bypassing the inks to get better information.
```python
from PyBypass import bypass

try:
    print(bypass("https://www40.zippyshare.com/v/DkywSXEu/file.html", name="zippyshare"))
    
except Exception as error:
    print(error)       
```


_____

<div align="center">
<h1><b>Some important points</b></h1>
</div>

- Some website change their code frequently so it is possible that this script stop bypasing those website link, i will try to keep it updated if possible.
- You have to provide required params like  ( gdtot_crypt, appdrive_email, appdrive_password, hubdrive_crypt, sharerepw_xsrf_token, sharerpw_larvel_token) to bypass gdrive sharer links. 
- I intentionally created different file for each bypassing scripts so that other user can easily copy paste that specific code if they want to use in their code.
- Please give proper credits and link this repo if you are using this library in any of your projects/bot.

______

<div align="center">
<h1><b>Credits and Contribution</b></h1>
</div>

This library used multiple scripts from  [@YukkiSenpai](https://github.com/xcscxr) github profile and [@zevtyardt](https://github.com/zevtyardt/lk21) lk21 respository.

------

  
<div align="center">
<h1><b>Copyright and License</b></h1>
</div>
<br>
<img src="https://telegra.ph/file/b5850b957f081cfe5f0a6.png" align="right" width="100">
  

* copyright (C) 2022 by [Sanjit sinha](https://github.com/sanjit-sinha)
* Licensed under the terms of the [The MIT License](https://github.com/sanjit-sinha/Telegram-Bot-Boilerplate/blob/main/LICENSE)

------
