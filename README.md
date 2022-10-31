<div align="center">
<h1>A library to bypass links</h1>
</div>

![PyBypass](https://telegra.ph/file/bfa59154e186c0ef3f3cf.jpg)


# PyBypass [BETA]

PyBasser is a python library wich can bypass various type of links and give you direct access to the content of the given link without getting bothered by annoying ads and shortlinks.

Currently it can bypass various types of shortlinks, filehosters, videoservers and gdrive sharer links.

https://pypi.org/project/PyBypass/


# Supported Website links

#### Shortners

try2link.com, adf.ly, bit.ly, ouo.io, ouo.press, shareus.in, shortly.xyz, tinyurl.com, thinfi.com, hypershort.com ,safeurl.sirigan.my.id, gtlinks.me, loan.kinemaster.cc, theforyou.in, linkvertise.com, shorte.st, earn4link.in, tekcrypt.in, link.short2url.in, go.rocklinks.net, rocklinks.net, earn.moneykamalo.com, m.easysky.in, indianshortner.in, open.crazyblog.in, link.tnvalue.in, shortingly.me, open2get.in, dulink.in, bindaaslinks.com, za.uy, pdiskshortener.com, mdiskshortner.link, go.earnl.xyz, g.rewayatcafe.com, ser2.crazyblog.in, bitshorten.com, rocklink.in, droplink.co, tnlink.in, ez4short.com, xpshort.com, vearnl.in, adrinolinks.in, techymozo.com, linkbnao.com, linksxyz.in, short-jambo.com, ads.droplink.co.in, linkpays.in, pi-l.ink, link.tnlink.in

### Filehoster

anonfiles.com, antfiles.com, 1fichier.com, gofile.io, hxfile.co, krakenfiles.com, mdisk.me, mediafire.com, pixeldrain.com, racaty.net, send.cm, sfile.mobi, solidfiles.com, sourceforge.net, uploadbaz.me, upload.ee, uppit.com, userscloud.com, we.tl, disk.yandex.com, zippyshare.com


#### VideoServers
fembed-hd.com, mp4upload.com, sltube.org, watchsb.com, streamtape.com

### Gdrivesharer

appdrive.info, new2.gdtot.sbs, hubdrive.me, sharer.pw
( appdrive lookalike dmains: driveapp.in, drivehub.in, gdflix.pro, drivesharer.in, drivebit.in, drivelinks.in, driveace.in, drivepro.in, gdflix.top )

# Installation Guide and How to use?

### Installation
```bash
 python -m pip install PyBypass
```
Updating Library 
```bash
python -m pip install --upgrade PyBypass
```

### How to use?
PyBypass is an library wich mean you can import them into your own application and use it accordingly.

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://www.mediafire.com/download/8nqmnblivkv6tk2")
```

#### To bypass gdrivesharer links you have to provide required parameters.
- gdtot take parameter gdtot_crypt
- hubdrive take parameter hubdrive_crypt
- sharer.pw take parameter sharerpw_xsrf_token and sharerpw_larvel_token
- appdive and it's lookalike doamins take parameter appdrive_email and appdrive_password. ( drive_id and folder_id are optional parameters)
- ( read comments of gdrivesharer scripts in https://github.com/sanjit-sinha/PyBypass/tree/main/PyBypass/GdriveSharer )

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://new2.gdtot.sbs/file/105111102182", gdtot_crypt="b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D")
```
#### some website have so many subdomains so it is hard to auto detect every link. use parameter name to bypass those type of links.
- some common website like those are adfly, linkvertise, short.st, appdrive 

```python
import PyBypass as bypasser

bypassed_link = bypasser.bypass("https://shorte.st/", name="shortest")
```



# Notes

- some website change their code frequently so it is possible that this script stop bypasing those website link, i will try to keep it updated if possible
- you have to provide required params like  ( gdtot_crypt, appdrive_email, appdrive_password, hubdrive_crypt, sharerepw_xsrf_token, sharerpw_larvel_token) to bypass gdrive sharer links. 
- i intentionally created different file for each bypassing scripts so that other user can easily copy paste that specific code if they want to use in their code.
- please give proper credits and link this repo if you are using this library in any of your projects/bot.


# credits and contribution

This library used multiple scripts from  [@YukkiSenpai](https://github.com/xcscxr) github profile and [@zevtyardt](https://github.com/zevtyardt/lk21) lk21 respository.

# About License
PyBypass is licensed under ![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
