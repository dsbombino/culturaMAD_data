import requests
# from bs4 import BeautifulSoup
from lxml import html

def get_image_src(link:str):
    '''
    Obtiene la url de la imagen que se encuentren en el enlace
    '''
    try:
        response = requests.get(link)
        tree = html.fromstring(response.content)

        # img = tree.xpath('//div[@class="tramites-content"]/div[1]/img/@src')
        # print(img)
        img = tree.xpath('//div[@class="image-content ic-right"]/img/@src')
        if len(img) > 0:
            return f'https://www.madrid.es{img[0]}'
        else:
            return 'No se pudo extraer la url'
    except Exception as e:
        return e
    
url = "https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=E0B06F450B4BA1D8757CA2348C422A93.app04; ROUTEID=.app04'
}

response = requests.request("GET", url, headers=headers, data=payload)

response_dict = response.json()

for item in response_dict['@graph']:
    link = item['link'].replace('http', 'https')
    print(type(link), link)
    img_src = get_image_src(link=link)
    print(img_src)
    # response = requests.get(link)
    # tree = html.fromstring(response.content)

    # img = tree.xpath('//div[@class="tramites-content"]/div[1]/img/@src')
    # print(img)
    

link = 'https://www.madrid.es/sites/v/index.jsp?vgnextchannel=ca9671ee4a9eb410VgnVCM100000171f5a0aRCRD&vgnextoid=4f3a40ec2fe7e810VgnVCM2000001f4a900aRCRD'
img_src = get_image_src(link=link)
print(img_src)