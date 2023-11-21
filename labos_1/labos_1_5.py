import requests

payload = {
    'temperatura' : 1000
}

response = requests.post('http://192.168.86.211/temperatura', json=payload)

print(response.status_code)
print(response.text)