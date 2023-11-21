from flask import Flask, request, redirect, url_for


app = Flask("Prva flask aplikacija")

@app.get('/')
def index():
    return 'Pocetna stranica'

@app.get('/login')
def login_page():
    return 'Stranica za prijavu'

@app.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_page'))
        

if __name__ == '__main__':
    app.run()