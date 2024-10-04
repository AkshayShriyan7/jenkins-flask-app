from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS and allow requests from specific origins
CORS(app, resources={r"/*": {"origins": ["http://localhost:7007", "http://0.0.0.0:7007"]}})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/catalog-info.yaml', methods=['GET', 'POST'])
def serve_yaml():
    directory = os.getcwd()  # Current working directory
    return send_from_directory(directory, 'catalog-info.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

