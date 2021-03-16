FROM python:3.8-slim-buster

LABEL maintainer="Jimmy chienfeng0719@hotmail.com"

ARG WORKDIR="app"
RUN apt-get update
RUN apt-get install -y vim tzdata bash
RUN mkdir -p ${WORKDIR}

ENV TZ=Asia/Taipei

WORKDIR ${WORKDIR}
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm requirements.txt