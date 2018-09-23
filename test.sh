#!/usr/bin/env bash

curl 'http://localhost:8080/v1/geocode?address=888+Brannan+Street+San+Francisco'
echo -e "\n\n"

curl "http://localhost:8080/v1/geocode?address=Rathausstra%C3%9Fe%2015,%2010178%20Berlin,%20Germany"
echo -e "\n\n"

curl "http://localhost:8080/v1/geocode?address=Somewhere+Only+We+Know"
echo -e "\n\n"

curl "http://localhost:8080/v1/geocode?address="
