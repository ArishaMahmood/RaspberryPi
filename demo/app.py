# /api4/app.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Aggregates data from other APIs
@app.route('/', methods=['GET'])
def get_server_run():
    message = "Flask server is running on port 5004"
    
    return message

if __name__ == '__main__':
    app.run(port=5004)
