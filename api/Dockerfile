FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/crm/api/

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	net-tools \
	sudo \
	bzip2 \
	curl \
	gcc \
	git \
	python3-dev \
	vim
RUN apt-get clean

ENV DJANGO_ENV develop
ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
