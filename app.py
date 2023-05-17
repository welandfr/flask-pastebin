import os
from flask import Flask, request, escape
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    ret = {'msg': 'Pastebin API endpoint /pastebin, needs key. POST as JSON: { "type": "str", "val": "your value" } (type can be omitted if str)' }

    return ret


pastebin = ['nothing here']
@app.route("/pastebin", methods = [ 'GET', 'POST' ])
def test_route():

    if request.args.get('api_key') != os.environ.get('API_KEY'):
        return { 'msg': 'ERROR: Bad API key' }, 401

    if request.method == 'GET':
        try:
            idx = int(request.args.get('idx') or 0)
            ret = { 
                'idx': idx,
                'type': 'str', 
                'val': escape(pastebin[idx]) 
            }
        except Exception as e:
            print(repr(e))
            ret = { 'msg': 'ERROR: GET failed' }, 500

    if request.method == 'POST':
        
        try:
            pasted_value = request.get_json()
            pastebin.insert(0, pasted_value['val'])
            ret = {'msg': 'OK'}

        except Exception as e:
            print(repr(e))
            ret = { 'msg': 'ERROR: POST failed (POST as JSON: { "type": "str", "val": "your value" } )' }, 500

    return ret

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
