from flask import Flask, Response
from flask import request
import json
import geo
from errors import NoResultException

app = Flask(__name__)


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/v1/geocode')
def geocode():
    address = request.args.get('address')

    try:
        lat, long, service = geo.query_lat_long_with_fallback(address)

        response_data = {
            'address': address,
            'lat': lat,
            'long': long,
            'service_provider': service,
        }
        js = json.dumps(response_data)

        return Response(js, status=200, content_type='application/json; charset=utf-8')
    except NoResultException:
        response_data = {
            'address': address,
            'error': "No geolocation can be found for such address",
        }
        js = json.dumps(response_data)

        return Response(js, status=404, content_type='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
