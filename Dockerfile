# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser myuser
USER myuser

CMD gunicorn webapp.wsgi:application --bind 0.0.0.0:$PORT
