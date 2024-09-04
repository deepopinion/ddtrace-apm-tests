#!/usr/bin/env just --justfile

set dotenv-load

run:
  @echo "Running without ddtrace..."
  @poetry run python main.py
  @echo "Running with ddtrace..."
  @poetry run ddtrace-run python main.py
