FROM python:3.10

COPY ./src /src
WORKDIR /src
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt