from credentials import data as creds
import json
import urllib


class GeocodingService(object):
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
        charsets = response.headers.get_charsets()
        text = response.read().decode(charsets[0])
        return self._parse_result(text)


class HereService(GeocodingService):
    _base_url = "https://geocoder.api.here.com/6.2/geocode.json"

    def _params(self):
        return {
            'app_id': creds.here_app_id,
            'app_code': creds.here_app_code,
            'searchtext': self.address,
        }

    def _parse_result(self, text):
        js = json.loads(text)
        latlong = js['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
        return latlong['Latitude'], latlong['Longitude']


class GoogleService(GeocodingService):
    _base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    def _params(self):
        return {
            'address': self.address,
            'key': creds.google_api_key,
        }

    def _parse_result(self, text):
        js = json.loads(text)
        latlong = js['results'][0]['geometry']['location']
        return latlong['lat'], latlong['lng']


