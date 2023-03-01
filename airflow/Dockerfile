FROM python:3.10.8-slim-buster

# TODO: optimize layers, multistage build, test build

ENV PYTHONUNBUFFERED 1
ENV POETRY_HOME="/opt/poetry"

COPY airflow/ /app
COPY ./pyproject.toml ./poetry.lock /app/
WORKDIR /app

RUN \
    apt-get update \
    && apt-get install -y\
      curl\
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - \
    && cd /usr/local/bin \
    &&  ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false



ARG DEV
ENV DEV ${DEV:-true}
RUN /bin/sh -c "if [ $DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 9000

ENTRYPOINT ["python3", "main.py", "server"]
