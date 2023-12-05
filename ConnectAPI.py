from flask import Flask, jsonify, request
import json
from predictDays import *
import numpy as np

app = Flask(__name__)

@app.route('/predictDay', methods=['POST'])
def predict():
    body = request.json
    dados = predictDays(body.get('days')).tolist()
    json_dados = json.dumps(dados)
    return jsonify({"json_dados":json_dados})

if __name__ == '__main__':
    app.run(debug=True)



