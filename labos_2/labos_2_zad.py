from flask import Flask, make_response, request

app = Flask("Prva flask aplikacija")

@app.get('/prvi_bod')
def prvi():
        resp = make_response('Uspjeh', 202)
        return resp
   
@app.get('/drugi_bod')
def drugi():
    json = {'broj_bodova' : 2}      
    return json

@app.delete('/treci_bod')
def treci():
    params = request.args.get('bodovi')
    resp = make_response('Uspjeh', params)
    return resp

@app.post('/cetvrti_bod')
def cetvrti():
    sk = request.json.get('bodovi')
    resp = make_response('Uspjeh', sk)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)