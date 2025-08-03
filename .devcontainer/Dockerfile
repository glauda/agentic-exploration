# Base image
FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Update system settings
RUN apt-get update && apt-get upgrade -y

# Intall uv
COPY --from=ghcr.io/astral-sh/uv:0.8.4 /uv /uvx /bin/
