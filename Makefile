PYTHON = python3
PIP := pip3

PROJECT := rvcs
ENTRY := $(PROJECT)/app.py

REQPROD := requirements/prod.txt
REQDEV := requirements/dev.txt
ENVDIR := ./venv
LOGDIR := ./logs
VIDEODIR := ./videos


install:
	mkdir logs
	$(PYTHON) -m venv $(ENVDIR)
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) install -r $(REQPROD);\
	$(PYTHON) setup.py install;\
)

local:
	mkdir logs
	$(PYTHON) -m venv $(ENVDIR)
	(\
	source $(ENVDIR)/bin/activate;\
	$(PIP) install -r $(REQDEV);\
	$(PYTHON) setup.py install develop;\
)

test:
	$(ENVDIR)/bin/$(PYTHON) setup.py test;\

run:
	$(ENVDIR)/bin/$(PROJECT)

clean:
	@echo "Cleaning...";
	pip3 uninstall -y rvcs
	$(RM) -r $(LOGDIR) $(VIDEODIR) build dist rvcs.egg-info
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

.PHONY: install test run clean
