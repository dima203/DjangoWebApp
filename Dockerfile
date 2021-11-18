# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET_KEY='django-insecure-w8l%ja)75#(ki!t5lnzzu@v!)mtg*+=g4ws7rbo6addx2t02ql'
ENV DJANGO_DEBUG=''
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
