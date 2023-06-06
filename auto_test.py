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
    dead_end = f'/api/v1/kits/{_id}/products'
    respons = r.post(url=_url+dead_end, json=produkty )
    return respons


def test():
    if auto(13,'https://284b3fc3-811b-40f7-a5b4-8f3cb6749ad0.serverhub.praktikum-services.ru',).status_code == 200:
        print('Done')
    else:
        print('Faild')
    
test()
