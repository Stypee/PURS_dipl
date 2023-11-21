from flask import Flask

app = Flask("Prva flask aplikacija")

@app.get('/')
def index():
    return 'Pocetna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

if __name__ == '__main__':
    app.run()