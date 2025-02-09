from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/drinks')
def get_drinks():
    return jsonify({'drinks': ['water', 'coffee', 'tea']})