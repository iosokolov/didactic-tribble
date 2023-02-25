FROM python:3.10.8-slim-buster

#RUN apt-get update && apt-get install -y \
#    libzbar0 \
#    libzbar-dev

ENV PYTHONUNBUFFERED 1
ENV POETRY_HOME="/opt/poetry"

COPY . /app
WORKDIR /app

RUN \
    apt-get update \
    && apt-get install \
      curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - \
    && cd /usr/local/bin \
    &&  ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false

COPY ../pyproject.toml ../poetry.lock* /app/

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 9001

ENTRYPOINT ["python3", "main.py"]
