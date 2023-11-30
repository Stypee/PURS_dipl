from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for

app = Flask("Prva flask aplikacija")

global list
list = [
    {'tekst': 'Prvi tekst'},
    {'tekst': 'Drugi tekst'},
    {'tekst': 'Treci tekst'},
]

@app.get('/')
def home_page():
    response = render_template('provjera.html', title='Početna stranica', testif='Poruka je poslana', tekstovi=list)
    
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)