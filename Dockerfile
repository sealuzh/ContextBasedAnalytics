FROM ubuntu:14.04

MAINTAINER Jurgen Cito "cito@ifi.uzh.ch"

RUN apt-get update && apt-get install python-pip -y -q

RUN mkdir -p /var/www/app
COPY . /var/www/app/

RUN pip install -r /var/www/app/requirements.txt 

EXPOSE 4000

CMD ["python", "/var/www/app/index.py"]
