# set the base image
FROM ubuntu:20.04

# File Author / Maintainer
MAINTAINER ImanMousaei

RUN apt-get -y update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

#set directoty where CMD will execute
WORKDIR /usr/src/bot

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]