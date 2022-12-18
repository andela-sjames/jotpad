ARG PYTHON_VERSION=3.9-slim-buster
FROM python:$PYTHON_VERSION

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

ARG BUILD_ENV=dev
ARG POETRY_VERSION=1.0.0

ENV BUILD_ENV="$BUILD_ENV"
ENV PYTHON_VERSION="$PYTHON_VERSION"

LABEL jotpad.distro.name=linux
LABEL jotpad.distro.release=debian
LABEL jotpad.image.name=jotpad-web
LABEL jotpad.build.env="$BUILD_ENV"
LABEL jotpad.python.version="$PYTHON_VERSION"

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    git \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*


RUN pip install "poetry==$POETRY_VERSION"

# setting locales
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# set work directory
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# load project files
COPY . /app

# create user and add to docker group
RUN adduser --disabled-password --gecos '' jotpad && \
    groupadd docker && \
    usermod -aG docker jotpad

# grant newly created user permissions on essential files
RUN chown -R jotpad:$(id -gn jotpad) /app/

# change user to newly created user
USER jotpad
