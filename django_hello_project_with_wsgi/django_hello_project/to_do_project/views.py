from flask import Flask, request, jsonify
app = Flask(__name__)
todos = []
@app.route('/todo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify(todo), 201
@app.route('/todo', methods=['GET'])
def get_todos():
    return jsonify(todos)
if __name__ == '__main__':
    app.run(debug=True)