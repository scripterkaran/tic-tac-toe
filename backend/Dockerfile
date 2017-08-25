FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /server
WORKDIR /server
ADD . requirements.txt /server/
RUN pip install -r requirements.txt
ADD . /server/