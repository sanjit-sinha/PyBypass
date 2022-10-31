"""
https?://(pixeldrain\.com\/(l|u)\/)\S+
https://pixeldrain.com/u/WeF9VBxQq
https://pixeldrain.com/l/ezRuCtHM
"""


def pixeldrain_bypass(pixeldrain_url: str) -> str:
    pixeldrain_url= pixeldrain_url[:-1] if pixeldrain_url[-1] == '/' else pixeldrain_url 
    file_id = pixeldrain_url.split("/")[-1]
    
    if pixeldrain_url.split("/")[-2] == "l":
        dl_link = f"https://pixeldrain.com/api/list/{file_id}/zip"
    else:
        dl_link = f"https://pixeldrain.com/api/file/{file_id}"
    return dl_link
     
        
