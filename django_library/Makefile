test:
	python manage.py test

lint:
	pylint $(shell git ls-files '*.py')

coverage:
	coverage run --source='.' manage.py test
	coverage html
	coverage report --fail-under=100