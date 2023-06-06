import requests as r

weather_parameters = {
    '0': '',
    'T':'',
    'M':'',
    'lang':'ru'
}
url = 'https://wttr.in/vanadzor'

response = r.get(url=url,params= weather_parameters)  

print(response.text)  