MANAGE_PY := ./moneybox/manage.py
KUBECTL := kubectl
MANIFESTS_PATH := .k8s/manifests

run:
	@echo "Running the application..."
	$(MANAGE_PY) runserver

migrate:
	@echo "Running migrations..."
	$(MANAGE_PY) makemigrations
	$(MANAGE_PY) migrate

createsuperuser:
	@echo "Creating superuser..."
	$(MANAGE_PY) createsuperuser

test:
	@echo "Running tests..."
	$(MANAGE_PY) test

gen-keyset:
	python gen_key.py

clear:
	@echo "Clearing cache..."
	rm -rf .ruff_cache

lint:
	@echo "Running linter..."
	black .
	ruff check .

clean-lint: lint clear
	@echo "Running linter and cleaning cache..."

# K8S
apply-k8s:
	@echo "Applying Kubernetes manifests..."
	$(KUBECTL) apply -f $(MANIFESTS_PATH)

delete-k8s:
	@echo "Deleting Kubernetes manifests..."
	$(KUBECTL) delete -f $(MANIFESTS_PATH)

diff-k8s:
	@echo "Showing differences in Kubernetes manifests..."
	$(KUBECTL) diff -f $(MANIFESTS_PATH)

validate-k8s:
	@echo "Validating Kubernetes manifests..."
	$(KUBECTL) apply --dry-run=client -f $(MANIFESTS_PATH)
