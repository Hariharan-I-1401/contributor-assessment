FROM python:3.13-slim-bookworm

WORKDIR /app

# Install git AND pytest
RUN apt-get update && apt-get install -y git
RUN pip install pytest==8.4.2

COPY setup.sh ./
COPY resources /app/resources

RUN bash /app/setup.sh

WORKDIR /app/personal-site