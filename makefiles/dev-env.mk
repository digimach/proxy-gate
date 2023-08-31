.PHONY: setup-python-venv

setup-python-venv :
	@echo "Creating python virtual environment"
	@python3 -m venv .venv
	@echo "Activating python virtual environment"
	@source .venv/bin/activate
	@echo "Installing python dependencies"
	@pip install -r requirements.txt
	@pip install -r requirements-test.txt
	@pip install -r requirements-lint.txt
	@echo "Done"
	@echo "To activate the virtual environment, run:"
	@echo "source venv/bin/activate"