from flask import Flask, request
import math
app = Flask(__name__)
@app.route('/sqrt')
def sqrt():
    n = float(request.args.get('n'))
    return {'sqrt': math.sqrt(n)}
if __name__ == '__main__':
    app.run(debug=True)