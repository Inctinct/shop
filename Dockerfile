FROM python:3.11

ENV PYTHONBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD=25Mdd2515!
ENV DJANGO_SETTINGS_MODULE=shop.settings

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .