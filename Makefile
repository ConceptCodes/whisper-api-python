MSG ?= "DB Migration"
HOST ?= "0.0.0.0"
PORT ?= "8080"

start:
	@python -m uvicorn app:main --reload --use-colors --timeout-keep-alive 300 --host $(HOST) --port $(PORT) --factory --timeout-graceful-shutdown 10

migrate:
	@echo "Creating migration"
	@python -m alembic revision --autogenerate -m $(MSG)
	@python -m alembic upgrade head

migrate-down:
	@echo "Rolling back migration"
	@python -m alembic downgrade -1