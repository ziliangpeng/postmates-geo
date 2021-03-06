from credentials import data as creds
import json
import urllib
from errors import NoResultException


class GeocodingService(object):
    """ This class abstracts a geo-coding service that can resolve lat-long given an address.

    Multiple locations could be found by a given search text from external services, along with richer
    information other than just a lat-long value. For simplicity, we only return a single lat-long pair
    from the first result (if present). The `_parse_query` method could be easily extended for parse richer
    information.
    """
    _base_url = "base_url_undefined"

    def __init__(self, address):
        self.address = address

    def _construct_url(self):
        return "%s?%s" % (self._base_url, urllib.parse.urlencode(self._params()))

    def _parse_result(self, text):
        raise NotImplementedError()

    def make_query(self):
        url = self._construct_url()
        print(url)
        response = urllib.request.urlopen(url, timeout=2)
        try:
            charset = response.headers.get_charsets()[-1]
        except IndexError:
            charset = 'utf-8'
        text = response.read().decode(charset)
        return self._parse_result(text)


class HereService(GeocodingService):
    """Implementation of proxying to Here service."""
    _base_url = "https://geocoder.api.here.com/6.2/geocode.json"

    def _params(self):
        return {
            'app_id': creds.here_app_id,
            'app_code': creds.here_app_code,
            'searchtext': self.address,
        }

    def _parse_result(self, text):
        js = json.loads(text)
        try:
            lat_long = js['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
        except (KeyError, IndexError):
            raise NoResultException()

        return lat_long['Latitude'], lat_long['Longitude'], 'Here'


class GoogleService(GeocodingService):
    """Implementation of proxying to Google service."""
    _base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    def _params(self):
        return {
            'address': self.address,
            'key': creds.google_api_key,
        }

    def _parse_result(self, text):
        js = json.loads(text)
        try:
            lat_long = js['results'][0]['geometry']['location']
        except (KeyError, IndexError) as e:
            raise NoResultException()

        return lat_long['lat'], lat_long['lng'], 'Google'


def query_lat_long_with_fallback(address):
    """ Make a query for latlong from address with fallback mechanism.

    The method will first attempt to query latlong from Google geocoding service for it's higher precision. If the server cannot
    connect to the Google service or a timeout happens, the server tries to route the query to the HERE geocoding service.

    Note: If Google service returns empty result, the server will also trigger fallback."""
    try:
        return GoogleService(address).make_query()
    except Exception:
        return HereService(address).make_query()
