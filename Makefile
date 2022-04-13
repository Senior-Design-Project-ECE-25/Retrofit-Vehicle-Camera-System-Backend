PYTHON = python3
PIP := pip3

REQ  := requirements.txt
REQLOC := requirements-dev.txt
ENVDIR := ./venv
LOGDIR := ./logs

local:
	$(PYTHON) -m venv $(ENVDIR)
	( source $(ENVDIR)/bin/activate; $(PIP) install -r $(REQLOC); )

install:
	$(PYTHON) -m venv $(ENVDIR)
	( source $(ENVDIR)/bin/activate; $(PIP) install -r $(REQ); )

# test:
# 	$(ENVDIR)/bin/$(PYTHON) rvcs/tests/tests.py

run:
	$(ENVDIR)/bin/$(PYTHON) rvcs/app.py

clean:
	@echo "Cleaning...";
	$(RM) -r $(LOGDIR)

.PHONY: install test run clean
