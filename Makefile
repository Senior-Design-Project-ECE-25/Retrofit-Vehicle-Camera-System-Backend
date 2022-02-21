PYTHON = python3
PIP := pip3

REQ  := requirements.txt
ENVDIR := ./env
LOGDIR := ./logs

install:
	$(PYTHON) -m venv $(ENVDIR)
	( source $(ENVDIR)/bin/activate; $(PIP) install -r $(REQ); )

test:
	$(ENVDIR)/bin/$(PYTHON) tests/tests.py

run:
	$(ENVDIR)/bin/$(PYTHON) app.py

clean:
	@echo "Cleaning...";
	$(RM) -r $(LOGDIR)

.PHONY: install test run clean
