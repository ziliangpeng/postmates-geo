from flask import Flask, Response
from flask import request
import json
import geo
from errors import NoResultException

app = Flask(__name__)


@app.route('/')
def hello():
    return "Postmates X\n"


@app.route('/geocode')
def geocode():
    address = request.args.get('address')

    try:
        lat, long, service = geo.query_lat_lang_with_fallback(address)

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
    app.run(port=8080)