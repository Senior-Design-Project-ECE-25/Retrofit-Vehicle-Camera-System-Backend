PYTHON = python3
PIP := pip3

PROJECT := rvcs
ENTRY := $(PROJECT)/app.py

REQPROD := requirements/prod.txt
REQDEV := requirements/dev.txt
ENVDIR := ./venv


install:
	$(PYTHON) -m venv $(ENVDIR)
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) install -r $(REQPROD);\
	$(PYTHON) setup.py install;\
)

develop:
	$(PYTHON) -m venv $(ENVDIR)
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) install -r $(REQDEV);\
	$(PYTHON) setup.py install develop;\
)

test:
	$(ENVDIR)/bin/$(PYTHON) -m unittest discover;

run:
	$(ENVDIR)/bin/$(PROJECT)

clean:
	@echo "Cleaning...";
	$(PIP) uninstall -y rvcs
	$(RM) -r logs videos build dist rvcs.egg-info
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

.PHONY: install test run clean
