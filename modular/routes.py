from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.root_path, 'templates/index.html')

@app.route('/api/message/get', methods=['GET'])
def getMessage():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)