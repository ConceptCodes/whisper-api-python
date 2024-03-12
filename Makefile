HOST ?= "0.0.0.0"
PORT ?= "8080"

start:
	@python -m uvicorn main:app --reload --use-colors --timeout-keep-alive 300 --host $(HOST) --port $(PORT) --factory --timeout-graceful-shutdown 10

docker:
	@docker-compose -f docker-compose.yml up --build