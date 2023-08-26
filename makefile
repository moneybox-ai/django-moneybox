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

generateadmin:
	$(MANAGE_PY) admin_generator api > moneybox/api/admin.py

generateapi:
	 $(MANAGE_PY) generate api -f modelviewset --force

lint:
	black .
	ruff check .
