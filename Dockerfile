FROM node:latest

WORKDIR /opt/birpen
RUN mkdir -p /opt/birpen

ADD . /opt/birpen

RUN \
 apt-get update && \
 apt-get -y install python3 python3-pip && \
 python3 -m pip install -r requirements.txt --no-cache-dir

RUN \
 npm install yarn && \
 yarn install && \
 yarn build

RUN chmod +x /opt/birpen/docker_start.sh

EXPOSE 8000
