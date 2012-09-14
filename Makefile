clean:
	@find . -name "*.pyc" -delete

setup: deps settings syncdb

syncdb:
	$(VIRTUAL_ENV)/bin/python manage.py syncdb --noinput
	$(VIRTUAL_ENV)/bin/python manage.py migrate

deps:
	$(VIRTUAL_ENV)/bin/pip install -r dev_requirements.txt

settings:
	cp pylestras/local_settings.example.py pylestras/local_settings.py

run:
	@python manage.py runserver 0.0.0.0:8000

update:
	@git push heroku master

static:
	@heroku run  python manage.py collectstatic

deploy: update syncdb collectstatic

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
