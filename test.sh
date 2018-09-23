#!/usr/bin/env bash

curl -v 'http://localhost:8080/geocode?address=888+Brannan+Street+San+Francisco'

curl -v "http://localhost:8080/geocode?address=Rathausstra%C3%9Fe%2015,%2010178%20Berlin,%20Germany"

curl -v "http://localhost:8080/geocode?address=Somewhere+Only+We+Know"

