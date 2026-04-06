# Base image
FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Remove Yarn repo (not needed, causes GPG key errors)
RUN rm -f /etc/apt/sources.list.d/yarn.list

# Update system packages
RUN apt-get update && apt-get upgrade -y

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.8.4 /uv /uvx /bin/
