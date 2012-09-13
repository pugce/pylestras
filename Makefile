clean:
	@find . -name "*.pyc" -delete

setup: deps settings
	$(VIRTUAL_ENV)/bin/python manage.py syncdb --noinput

deps:
	$(VIRTUAL_ENV)/bin/pip install -r dev_requirements.txt

settings:
	cp pylestras/local_settings.example.py pylestras/local_settings.py

run:
	@python manage.py runserver 0.0.0.0:8000

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
