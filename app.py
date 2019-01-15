from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Word!'

@app.route('/test')
def hello_world():
    return 'test page!'

if __name__ == '__main__':
    app.run()
