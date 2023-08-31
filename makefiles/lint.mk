.PHONY: lint lint-flake8 lint-pylint lint-black black

lint : lint-flake8 lint-pylint lint-black

lint-flake8 :
	flake8 --count --statistics app/ *.py

lint-pylint :
	pylint --jobs 0 --fail-under 9.80 app/ *.py

lint-black :
	black --check --diff --verbose app/ *.py

black :
	black app/ *.py