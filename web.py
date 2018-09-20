from flask import Flask, Response
from flask import request
import json
import geo

app = Flask(__name__)


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/geocode')
def geocode():
    address = request.args.get('address')

    lat = None
    long = None

    here_response = geo.make_here_query(address).text
    google_response = geo.make_google_query(address).text

    response_data = {
        'address': address,
        'lat': lat,
        'long': long,
        'here': here_response,
        'google': google_response,
    }
    js = json.dumps(response_data)

    return Response(js, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(port=8080)
