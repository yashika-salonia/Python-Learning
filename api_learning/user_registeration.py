from flask import Flask, request, jsonify
app = Flask(__name__)
users = []
@app.route('/register', methods=['POST'])
def register():
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201
if __name__ == '__main__':
    app.run(debug=True)