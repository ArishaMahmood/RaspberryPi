# /api1/app.py
from flask import Flask, jsonify, request
import random
app = Flask(__name__)


@app.route('/random_number', methods=['GET'])
def get_user():
    random_number = random.randint(1, 200)
    return jsonify(random_number)

if __name__ == '__main__':
    app.run(port=5001)
