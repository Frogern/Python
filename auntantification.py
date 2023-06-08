import requests as r

login = "simpleForm@authenticationtest.com"
_pass = "pa$$w0rd"
_data = {
    'email': login,
    'password': _pass
}
url= "https://authenticationtest.com//login/?mode=simpleFormAuth"
user_agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
s = r.Session()
respons = s.post(url,data=_data)
print(respons.text)
print(respons.url)

