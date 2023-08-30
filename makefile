MANAGE_PY := ./moneybox/manage.py

run:
	$(MANAGE_PY) runserver

migrate:
	$(MANAGE_PY) makemigrations
	$(MANAGE_PY) migrate

createsuperuser:
	$(MANAGE_PY) createsuperuser

loaddata:
	$(MANAGE_PY) loaddata api/fixtures/currency.json

resetdb:
	rm db.sqlite3
	$(MANAGE_PY) migrate

test:
	$(MANAGE_PY) test

lint:
	black .
	ruff check .
