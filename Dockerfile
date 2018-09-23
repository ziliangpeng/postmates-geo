FROM python:3.6-alpine
MAINTAINER Victor Z. Peng

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "web.py"]