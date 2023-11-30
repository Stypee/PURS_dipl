from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for

app = Flask("Prva flask aplikacija")
app.secret_key ='22_x_11_y_99_z#1911th'

@app.before_request
def before_request_funkcija():
    if request.path == '/login':
        return
    
    if session.get('username') is None:
        return redirect(url_for('login_page'))

@app.get('/')
def home_page():
    response = render_template('index.html')

    return response, 200

@app.get('/login')
def login_page():
    response = render_template('login.html')

    return response, 200

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login_page'))

@app.post('/login')
def login():
    response = make_response()

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'STIPE' and password == '221199':
        session['username'] = username

        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


    