from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/doubler')
def doubler():
    return str([2*x for x in range(5)])
