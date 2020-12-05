FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

WORKDIR /app/

# Install Poetry
RUN wget -q -O - https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN ln -s ${HOME}/.poetry/bin/poetry /bin/poetry
RUN poetry config virtualenvs.create false

RUN apk update
RUN apk add --upgrade hiredis
# Copy poetry.lock* in case it doesn't exist in the repo
# COPY ./pyproject.toml ./poetry.lock* /app/
COPY . /app

RUN poetry install --no-root --no-dev
ENV PYTHONPATH=/app