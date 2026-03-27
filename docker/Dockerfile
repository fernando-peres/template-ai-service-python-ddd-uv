# syntax=docker/dockerfile:1.6

## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.13-alpine AS builder


# Install dependencies using Alpine's package manager
RUN apk add --no-cache \
    build-base \
    curl \
    openssh  # for ssh-keyscan

## Download the latest installer, install it and then remove it
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

## Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

## Create the application directory
WORKDIR /app

## Copy dependency files for layer caching
COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./README.md .

RUN uv sync --frozen --no-dev

## ------------------------------- Production Stage ------------------------------ ##
FROM python:3.13-alpine AS production

## Add non-root user using Alpine utilities
RUN adduser -D -h /home/appuser appuser
USER appuser
WORKDIR /app

COPY --chown=appuser:appuser ./service ./service
COPY --chown=appuser:appuser --from=builder /app/.venv .venv
COPY --chown=appuser:appuser main.py .

ENV PYTHONPATH=/app/service
ENV PATH="/app/.venv/bin:$PATH"

ARG PORT=8080
EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn main:create_service --factory --log-level info --host ${HOST_IP:-0.0.0.0} --port ${PORT:-8080}"]
