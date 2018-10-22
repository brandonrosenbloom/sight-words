FROM python:3.6
# Based on https://hub.docker.com/_/buildpack-deps/

MAINTAINER Aaron McMillin

# Expose ports
EXPOSE 80 8000

# No more warnings!
ENV DEBIAN_FRONTEND noninteractive

# Set the default directory where CMD will execute
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# System Deps
RUN apt-get update && apt-get install -qq -y postgresql-client && apt-get clean

# Requirements.txt alone for caching
ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

ADD . /usr/src/app/

ENTRYPOINT ["/usr/src/app/manage.py"]