from credentials import data as creds
import requests


def construct_here_url(address):
    address = address.replace(' ', '+')
    return "https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=%s" % (creds.here_app_id, creds.here_app_code, address)

def construct_google_url(address):
    raise NotImplementedError()


def make_here_query(address):
    url = construct_here_url(address)
    print(url)
    return requests.get(url)



def make_google_query(address):
    raise NotImplementedError()
