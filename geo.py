from credentials import data as creds
import json
import urllib


class GeocodingService(object):
    def __init__(self, address):
        self.address = address.replace(' ', '+')

    def _construct_url(self):
        raise NotImplementedError()

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
    def _construct_url(self):
        return "https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=%s" % (creds.here_app_id, creds.here_app_code, self.address)

    def _parse_result(self, text):
        js = json.loads(text)
        latlong = js['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
        return latlong['Latitude'], latlong['Longitude']


class GoogleService(GeocodingService):
    def _construct_url(self):
        return "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (self.address, creds.google_api_key)

    def _parse_result(self, text):
        js = json.loads(text)
        latlong = js['results'][0]['geometry']['location']
        return latlong['lat'], latlong['lng']


