from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/geocode')
def geocode():
    address = request.args.get('address')
    return "%s\n" % address


if __name__ == '__main__':
    app.run(port=8080)
