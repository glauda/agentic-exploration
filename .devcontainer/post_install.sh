#!/bin/sh

# Setup venv
if [[ ! -d .venv ]]; then
    echo "Creating virtual environment"
    uv venv
fi

echo "Updating dependencies"
uv sync

# Setup git credentials
git config --global user.email "florent-glauda@orange.fr"
git config --global user.name "Florent Glauda"

echo "Devcontainer setup completed successfully!"
