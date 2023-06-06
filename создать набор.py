import requests as r 
_params = {
    "cardId" : 3,
    "name" : "Тест"
}

server_url = 'https://284b3fc3-811b-40f7-a5b4-8f3cb6749ad0.serverhub.praktikum-services.ru'
end_point = '/api/v1/kits'

respons = r.post(url=server_url+end_point,json=_params)
print(respons.text)