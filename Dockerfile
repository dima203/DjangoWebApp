# syntax=docker/dockerfile:1
FROM python:3.10

ENV http_proxy http://proxy-chain.xxx.com:911/
ENV http_proxy http://proxy-chain.xxx.com:912/

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0

COPY ./requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser myuser
USER myuser

CMD gunicorn webapp.wsgi:application --bind 0.0.0.0:$PORT
