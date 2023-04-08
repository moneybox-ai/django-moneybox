MANAGE_PY := ./moneybox/manage.py

# Запуск приложения
run:
	$(MANAGE_PY) runserver

# Создание миграций
migrate:
	$(MANAGE_PY) makemigrations
	$(MANAGE_PY) migrate

# Создание суперпользователя
createsuperuser:
	$(MANAGE_PY) createsuperuser

# Создание тестовых данных
loaddata:
	$(MANAGE_PY) loaddata fixtures/*.json

# Удаление базы данных
resetdb:
	rm db.sqlite3
	$(MANAGE_PY) migrate

# Запуск тестов
test:
	$(MANAGE_PY) test

# Генерация админки
generateadmin:
	$(MANAGE_PY) admin_generator api >> moneybox/api/admin.py

# Генерация API
generateapi:
	 $(MANAGE_PY) generate api -f modelviewset --force