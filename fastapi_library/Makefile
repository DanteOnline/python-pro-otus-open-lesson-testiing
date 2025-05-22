test:
	pytest

run:
	uvicorn main:app --reload

init_db:
	python init_db.py

lint:
	pylint $(shell git ls-files '*.py')

coverage:
	pytest -s --cov --cov-report html --cov-fail-under 100