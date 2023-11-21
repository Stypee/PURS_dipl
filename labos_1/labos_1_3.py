import requests

payload = {
   "username" : "PURS" ,
   "password" : "1234" 
}

response = requests.post('http://127.0.0.1:5000/login', json=payload)

print(response.text)
print(response.status_code)

