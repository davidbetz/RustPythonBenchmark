VENV_NAME := env
PYTHON := $(VENV_NAME)/bin/python
PIP := $(VENV_NAME)/bin/pip

.PHONY:

all:

run:
	@$(PYTHON) main.py

setup:
	@python3.11 -m venv $(VENV_NAME)
	@echo "Virtual environment created."

install: setup
	@$(PIP) install -r requirements.txt
	@$(PYTHON) -m pip install --upgrade pip
	@echo "Dependencies installed."

