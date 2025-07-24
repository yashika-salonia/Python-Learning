from flask import Flask
app = Flask(__name__) #can write my name

@app.route('/') #default route
def home():
    return "Hello, World ji!"
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask
# app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}!"


if __name__ == '__main__': #main is file name
    app.run(debug=True)