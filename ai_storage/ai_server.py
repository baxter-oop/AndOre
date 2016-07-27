from flask import Flask, request, jsonify, url_for, render_template, make_response, redirect, current_app
import database_functions

app = Flask(__name__)

web_server_domain = "*"


def home_cor(obj):
    return_response = make_response(obj)
    return_response.headers['Access-Control-Allow-Origin'] = web_server_domain
    return_response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Origin"
    return return_response


@app.route('/retrieve')
def retrieve():
    mid = request.args.get('mid', '')
    response = {
        'model': database_functions.retrieve_model(mid)
    }
    return home_cor(jsonify(**response))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data = request.json
    mid = request.args.get('mid', '')
    model = data.get('model', '')
    response = {
        'response': database_functions.save_model(mid, model)
    }
    return home_cor(jsonify(**response))

app.run(debug=True, host='0.0.0.0', port=7003, threaded=True)