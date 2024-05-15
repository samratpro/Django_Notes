FROM python:3.11-alpine

RUN apk update \
    && apk add --no-cache postgresql-client \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Set the ALLOWED_HOSTS environment variable
ENV ALLOWED_HOSTS=localhost,127.0.0.1
WORKDIR /app

COPY ./setup.sh /
ENTRYPOINT ["sh", "/setup.sh"]
