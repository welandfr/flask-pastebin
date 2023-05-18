import os
from flask import Flask, request, escape
from flask_cors import CORS 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

pastebin = []

def get_val(idx):
    try:
        ret = { 
            'idx': idx,
            'type': 'str', 
            'val': escape(pastebin[idx]),
            'len': len(pastebin)
        }
    except IndexError as e:
        print(repr(e))
        ret = { 'msg': f"No value found at index {idx}" }, 400
    except Exception as e:
        print(repr(e))
        ret = { 'msg': 'ERROR: GET failed' }, 500

    return ret


@app.route("/")
def index():
    ret = {'msg': 'Pastebin API endpoint /pastebin?api_key=<api-key>. POST as JSON: { "type": "str", "val": "your value" } (type can be omitted if str)' }

    return ret

@app.route("/pastebin/<int:idx>", methods = [ 'GET', 'DELETE' ])
def pastebin_idx_route(idx):

    if request.args.get('api_key') != os.environ.get('API_KEY'):
        return { 'msg': 'ERROR: Bad API key' }, 401

    if request.method == 'GET':
        ret = get_val(idx)

    if request.method == 'DELETE':
        try:
            pastebin.pop(idx)
            ret = {'msg': 'Value removed.'}
        except IndexError as e:
            print(repr(e))
            ret = { 'msg': f"No value found at index {idx}" }, 400
        except Exception as e:
            print(repr(e))
            ret = { 'msg': 'ERROR: DELETE value failed' }, 500

    return ret

@app.route("/pastebin", methods = [ 'GET', 'POST', 'DELETE' ])
def pastebin_route():

    if request.args.get('api_key') != os.environ.get('API_KEY'):
        return { 'msg': 'ERROR: Bad API key' }, 401

    if request.method == 'GET':
        ret = get_val(0)

    if request.method == 'POST':

        try:
            pasted_value = request.get_json()
            pastebin.insert(0, pasted_value['val'])
            ret = {'msg': 'OK'}

        except Exception as e:
            print(repr(e))
            ret = { 'msg': 'ERROR: POST failed.' }, 500

    if request.method == 'DELETE':
        try:
            pastebin.clear()
            ret = {'msg': 'Pastebin cleared.'}
        except Exception as e:
            print(repr(e))
            ret = { 'msg': 'ERROR: DELETE failed.' }, 500

    return ret

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
