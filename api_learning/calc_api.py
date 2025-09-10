from flask import Flask, request, jsonify
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()
app = Flask(__name__)
@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'sum': a + b})
if __name__ == '__main__':
    app.run(debug=True)