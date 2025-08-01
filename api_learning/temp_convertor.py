from flask import Flask, request
app = Flask(__name__)
@app.route('/c2f')
def celsius_to_fahrenheit():
    c = float(request.args.get('c'))
    f = (c * 9/5) + 32
    return {'fahrenheit': f}
if __name__ == '__main__':
    app.run(debug=True)