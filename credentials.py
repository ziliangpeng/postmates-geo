import json

CREDENTIALS_FILE = "credentials.json"


SERVICE_HERE = 'here'
SERVICE_GOOGLE = 'google'
KEY_APP_ID = 'app_id'
KEY_APP_CODE = 'app_code'
KEY_API_KEY = 'api_key'


class GeoServicesCredentials:

    def _validate_credential(self, service, key):
        if service not in self.js or key not in self.js[service]:
            raise Exception("key %s for service %s not found" % (key, service))
        value = self.js[service][key]
        if type(value) is not str:
            raise Exception("key %s for service %s should be str" %
                            (key, service))

    def __init__(self, js):
        self.js = js
        self._validate_credential(SERVICE_HERE, KEY_APP_ID)
        self._validate_credential(SERVICE_HERE, KEY_APP_CODE)
        self._validate_credential(SERVICE_GOOGLE, KEY_API_KEY)
        self.here_app_id = js[SERVICE_HERE][KEY_APP_ID]
        self.here_app_code = js[SERVICE_HERE][KEY_APP_CODE]
        self.google_api_key = js[SERVICE_GOOGLE][KEY_API_KEY]


def read_credentials():
    """ Reads the secrets from file and return a GetServicesCredentials object to hold all the secrets."""
    with open(CREDENTIALS_FILE, 'r') as f:
        content = f.read()
        js = json.loads(content)
        return GeoServicesCredentials(js)


data = read_credentials()
