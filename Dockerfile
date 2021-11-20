# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
RUN adduser -D myuser
USER myuser
CMD gunicorn webapp.wsgi:application --log-file - --log-level debug
