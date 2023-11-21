from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for

app = Flask("Prva flask aplikacija")

@app.get('/test')
def test_page():
    response = render_template('test.html')

    return response

@app.post('/unos_korisnika')
def unos_korisnika():
    response = make_response()

    text = request.form.get('text')
    password = request.form.get('password')

    response.data = f'Text: {text} Password: {password}'

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)