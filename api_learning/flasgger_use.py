from flask import Flask, jsonify, request
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
@app.route('/multiply')
def multiply():
    """Multiply two numbers
    ---
    parameters:
      - name: a
        in: query
        type: integer
        required: true
      - name: b
        in: query
        type: integer
        required: true
    responses:
      200:
        description: Result
    """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'result': a * b})
if __name__ == '__main__':
    app.run(debug=True)