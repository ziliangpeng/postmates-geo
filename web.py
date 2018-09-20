from flask import Flask, Response
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/geocode')
def geocode():
    address = request.args.get('address')

    lat = None
    long = None

    response_data = {
        'address': address,
        'lat': lat,
        'long': long,
    }
    js = json.dumps(response_data)

    return Response(js, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(port=8080)
