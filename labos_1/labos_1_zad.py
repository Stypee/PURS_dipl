import requests

payload = {
    'ime' : 'Stipe',
    'prezime' : 'Karuza',
    'ip' : '192.168.86.212'
}

params = {
    'id' : 202
}

response = requests.get('http://192.168.86.210/jupiii')

print(response.text)

for k, v in response.headers.items():
    print(f'{k}: {v}')



