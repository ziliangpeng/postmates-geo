# Geocoding Service

This is a simple proxy that does lat-long look up from a given address, backed by external geocoding services.

This service relies on 2 external services: Google, and Here. When processing query requests, it will first attemps to resolve lat-long using the Google service, if failure happens, it will fall back to using here service.

## How to run the service

Please follow these steps for running the service

### Secret Injection

Create a `credentials.json` from `credentials.json.example`

``` 
cp credentials.json.example credentials.json
```

Then put in your API secrets into corresponding fields in the json file. You must first obtain API token from HERE and Google service in order to run this service.


### Starting The Service

There are several ways of running the service

#### running natively

You must use `python 3` to run the service natively, and make sure `flask` is installed

```
pip install flask
python web.py
```

#### running via Docker

a Dockerfile is provided that prepares the correct environment to run this service inside a container.

```
docker build -t pm-geo .
docker run -p 8080:8080 pm-geo
```

#### running via docker-compose

You can also run it using docker-compose, for all the pre-baked settings.

```
docker-compose up --build geo
```

## How to use the service

To use the service, simple hit the REST endpoint `/v1/geocode?address={YourAddress}`.

For example, if you are running the service locally, you can hit the endpoint like this:

```
curl http://localhost:8080/v1/geocode?address=888+Brannan+Street+San+Francisco
```

You will get a response in json format, like this:

```
{
  address: "888 Brannan San Francisco",
  lat: 37.7719769,
  long: -122.4050479,
  service_provider: "Google"
}
```

More examples can be found in `test.sh`.

