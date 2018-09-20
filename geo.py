from credentials import data as creds
import requests


class GeocodingService(object):
    def __init__(self, address):
        self.address = address.replace(' ', '+')

    def _construct_url(self):
        raise NotImplementedError()

    def make_query(self):
        url = self._construct_url()
        print(url)
        return requests.get(url)


class HereService(GeocodingService):
    def _construct_url(self):
        return "https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=%s" % (creds.here_app_id, creds.here_app_code, self.address)


class GoogleService(GeocodingService):
    def _construct_url(self):
        return "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (self.address, creds.google_api_key)


