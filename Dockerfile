# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser myuser
USER myuser

CMD gunicorn webapp.wsgi:application --bind 0.0.0.0:$PORT
