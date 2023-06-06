import requests 

xml_file = """<InputModel>
                     #<productsCount>2</productsCount>
                     #<productsWeight>5.1</productsWeight>
                     #<deliveryTime>20</deliveryTime>
                 #</InputModel>"""
heads = {'Content-Type' : 'application/xml'}

url_fix='https://70cc9a9c-16bc-4dae-a1fe-0a50b1f3e9fa.serverhub.praktikum-services.ru'
def auto(_url):
    dead_end = '/fast-delivery/v3.1.1/calculate-delivery.xml'
    respons = requests.post(url=_url+dead_end, data=xml_file, headers=heads)
    return respons
print(auto(url_fix).text)