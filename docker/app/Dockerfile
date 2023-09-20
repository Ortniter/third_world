FROM python:3.11.5-slim-bullseye
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev python-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/ requirements/
RUN pip install --upgrade pip
RUN pip install -r requirements/base.txt --src=/root/pip
COPY docker/app/wait-for.sh /usr/local/bin/wait-for
