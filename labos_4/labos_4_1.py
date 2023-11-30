from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for
import jinja2

app = Flask("Prva flask aplikacija")
app.secret_key ='22_x_11_y_99_z#1911th'

global list
list_temp = [
    {   'datum': '27.11.2023.',
         'vrijednost': 20
    },
    {   'datum': '26.11.2023.',
        'vrijednost': 16
    },
    {   'datum': '25.11.2023.',
        'vrijednost': 14
    },
    {   'datum': '24.11.2023.',
        'vrijednost': 15
    },
]

list_vlaga = [
    {   'datum': '22.11.2023.',
         'vrijednost': 64
    },
    {   'datum': '21.11.2023.',
        'vrijednost': 59
    },
    {   'datum': '20.11.2023.',
        'vrijednost': 60
    },
    {   'datum': '19.11.2023.',
        'vrijednost': 69
    },
]

@app.before_request
def before_request_funkcija():
    if request.path == '/login':
        return
    
    if session.get('username') is None:
        return redirect(url_for('login_page'))

@app.get('/')
def home_page():
    id = request.args.get('id')
    if id == '1' or id == None:
        response1 = render_template('index.html', title='Početna stranica', naziv=session['username'], data=list_temp, tip='Temperatura')
        return response1, 200
    
    elif id == '2':
        response2 = render_template('index.html', title='Početna stranica', naziv=session['username'], data=list_vlaga, tip='Vlaga')
        return response2, 200


@app.get('/login')
def login_page():
    response = render_template('login.html', title='Login stranica')

    return response, 200


@app.get('/logout')
def logout_page():
    session.pop('username')

    return redirect(url_for('login_page'))


@app.post('/login')
def login():
    response = make_response()

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'stipe' and password == '221199':
        session['username'] = username

        return redirect(url_for('home_page'))
    else:
        return render_template('login.html', title='Login stranica', poruka='Uneseni su pogrešni podaci')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
