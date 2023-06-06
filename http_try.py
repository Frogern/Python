import requests
import json
cookies = dict(cookies_are='working')
products = {"deliveryTime": 9,"productsCount": 10,"productsWeight": 11}
dead_end=''
_linq = 'https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=philipkiely%2Fdjango_taskmanager' 
url=_linq+dead_end
r = requests.post(url,cookies=cookies)
print(r) 
print(r.text)