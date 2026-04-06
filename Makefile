.PHONY: install start lint clean

install:
	uv sync

start:
	adk web

lint:
	uv run ruff check .
