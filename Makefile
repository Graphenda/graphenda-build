.PHONY: install lint format test test-integration test-cov clean docker-up docker-down

install:
	pip install -e ".[dev,test]"
	pre-commit install || true

lint:
	ruff check graphenda_build/ scripts/ tests/
	mypy graphenda_build/

format:
	black graphenda_build/ scripts/ tests/
	isort graphenda_build/ scripts/ tests/
	ruff check --fix graphenda_build/ scripts/ tests/

test:
	pytest tests/ -v -m "not integration"

test-integration:
	pytest tests/ -v -m integration

test-cov:
	pytest tests/ -m "not integration" --cov=graphenda_build --cov-report=term-missing --cov-report=html

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist *.egg-info

docker-up:
	docker compose up -d

docker-down:
	docker compose down
