APP_PACKAGE := grocerylist
WSGI_APP := $(APP_PACKAGE).wsgi:application
GUNICORN_DEV_CONF := config/gunicorn.dev.conf.py
GUNICORN_PROD_CONF := config/gunicorn.prod.conf.py

.PHONY: run
run:
	export FLASK_APP=$(APP_PACKAGE) && \
	export FLASK_DEBUG=true && \
	flask run --host=0.0.0.0 --port=5000

.PHONY: start
start:
	gunicorn --config $(GUNICORN_DEV_CONF) $(WSGI_APP)

.PHONY: test
test:
	python -m unittest

.PHONY: lint
lint:
	pylint $(APP_PACKAGE)
