FROM python:3.6

# Update system and install curl.
RUN apt-get update && apt-get -y install build-essential curl

# Install python dependencies early to leverage docker cache.
COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install \
    --requirement /opt/app/requirements.txt

# Copy django app.
WORKDIR /opt/app
RUN mkdir ./logs
COPY . /opt/app
