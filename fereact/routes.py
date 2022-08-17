from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='build', static_url_path='/')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('build', 'index.html')

@app.route('/api/message/get', methods=['GET'])
def getMessage():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)