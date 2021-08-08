FROM postgres:13-alpine

RUN apk add python3 py3-pip 
RUN pip install kaggle
