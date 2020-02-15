FROM python:3.8.1-alpine3.11
MAINTAINER Ravan Nannapaneni

ENV PYTHONUNBUFFERED 1

RUN apk add vim

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app


