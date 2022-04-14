PYTHON = python3
PIP := pip3

REQPROD := requirements/prod.txt
REQDEV := requirements/dev.txt
ENVDIR := ./venv
LOGDIR := ./logs
VIDEODIR := ./videos

install:
	$(PYTHON) -m venv $(ENVDIR)
	( source $(ENVDIR)/bin/activate; $(PIP) install -r $(REQPROD); )

local:
	$(PYTHON) -m venv $(ENVDIR)
	( source $(ENVDIR)/bin/activate; $(PIP) install -r $(REQDEV); )

test:
	$(ENVDIR)/bin/$(PYTHON) -m unittest tests

run:
	$(ENVDIR)/bin/$(PYTHON) app.py

clean:
	@echo "Cleaning...";
	$(RM) -r $(LOGDIR) $(VIDEODIR)
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

.PHONY: install test run clean
