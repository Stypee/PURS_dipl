from flask import Flask, request, make_response

temperatura = []

app = Flask("Prva flask aplikacija")

@app.post('/temperatura')
def tijelo():
    global temperatura
    temp = request.json.get('temperatura')

    if  temp is not None:
        temperatura.append(temp)
        resp = make_response('Uspješno ste postavili temperaturu', 201)
        return resp
    else:
        resp = make_response('Niste upisali ispravan ključ', 404)
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)