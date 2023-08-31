# pull the official docker image
FROM python:3.10.13-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

# copy project
COPY ./app ./
