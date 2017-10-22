.PHONY: run
run:
	export FLASK_APP=grocerylist && \
	export FLASK_DEBUG=true && \
	flask run --host=0.0.0.0 --port=5000

.PHONY: test
test:
	python -m unittest
