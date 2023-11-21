import requests

response = requests.get('http://192.168.86.211/temperatura')



if response.headers.get('Content-Type') == 'application/json':
    print(response.json().get("temperatura"))
