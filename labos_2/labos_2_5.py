from flask import Flask, request, make_response

temperatura = []

app = Flask("Prva flask aplikacija")

@app.post('/temperatura')
def provjeri_temp():
    global temperatura
    temp = request.json.get('temperatura')

    if  temp is not None:
        temperatura.append(temp)
        resp = make_response('Uspješno ste postavili temperaturu', 201)
        return resp
    else:
        resp = make_response('Niste upisali ispravan ključ', 404)
        return resp

@app.get('/temperatura')
def vrati_temp():
    payload = {'temperatura' : temperatura[-1]}
    return payload

@app.delete('/temperatura')
def obrisi_temp():
    params = request.args.get('id')

    if params is not None:
        if int(params) <= len(temperatura-1):
            del temperatura[int(params)]
            return 'Uspjesno ste obrisali temperaturu', 202
        else:
            return 'Upisali ste neispravan ključ', 404
    else:
        return 'Upisali ste neispravan ključ', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)