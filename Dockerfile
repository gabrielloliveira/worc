FROM python:3.8.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip3 install -U pip setuptools

COPY requirements.txt /app/

RUN pip3 install -r /app/requirements.txt

ADD . /app/

EXPOSE 8000