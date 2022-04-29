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
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) uninstall -y rvcs;\
)
	$(RM) -r $(ENVDIR)/lib/python3.*/site-packages/$(PROJECT)
	$(RM) -r ./build ./dist ./rvcs.egg-info
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

.PHONY: install develop test run clean
