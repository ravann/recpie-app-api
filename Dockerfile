FROM python:3.8.1-alpine3.11
MAINTAINER Ravan Nannapaneni

ENV PYTHONUNBUFFERED 1

RUN apk add vim

COPY requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /tmp/requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app

WORKDIR /app

COPY ./app /app


