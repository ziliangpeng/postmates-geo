from flask import Flask, Response
from flask import request
import json
import geo
from errors import NoResultException

app = Flask(__name__)


def make_response(status_code, js):
    return Response(json.dumps(js), status=status_code, content_type='application/json; charset=utf-8')


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/v1/geocode')
def geocode():
    address = request.args.get('address').strip()
    if address == "":
        return make_response(400, {'error': "address cannot be empty"})

    try:
        lat, long, service = geo.query_lat_long_with_fallback(address)

        response_data = {
            'address': address,
            'lat': lat,
            'long': long,
            'service_provider': service,
        }
        return make_response(200, response_data)
    except NoResultException:
        response_data = {
            'address': address,
            'error': "No geolocation can be found for such address",
        }
        return make_response(404, response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
