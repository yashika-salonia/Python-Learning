from flask import Flask
import datetime
app = Flask(__name__)
@app.route('/time')
def get_time():
    return {'time': datetime.datetime.now().isoformat()}
if __name__ == '__main__':
    app.run(debug=True)