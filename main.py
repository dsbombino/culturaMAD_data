import requests

url = "https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=E0B06F450B4BA1D8757CA2348C422A93.app04; ROUTEID=.app04'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
