SHELL := /bin/bash
PYTHON = python3
PIP := pip3

ENVDIR := ./venv

PROJECT := rvcs
TARGET := $(ENVDIR)/bin/$(PROJECT)

install:
	$(PYTHON) -m venv $(ENVDIR)
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) install --upgrade pip setuptools wheel;\
	$(PIP) install .;\
)

test:
	$(ENVDIR)/bin/$(PYTHON) -m unittest discover;

run:
	$(TARGET) run

clean:
	@echo "Cleaning...";
	$(PIP) uninstall -y rvcs
	$(RM) -r logs videos build dist rvcs.egg-info
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

.PHONY: install develop test run clean
