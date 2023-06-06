import requests as r 

produkty = {
    'productsList' : [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}


def auto(_id,_url):
    end_point = f'/api/v1/kits/{_id}/products'
    respons = r.post(url=_url+end_point, json=produkty )
    return respons


def test():
    if auto(13,'https://284b3fc3-811b-40f7-a5b4-8f3cb6749ad0.serverhub.praktikum-services.ru',).status_code == 200:
        return 'Done'
    return 'Faild'
    
print(test())