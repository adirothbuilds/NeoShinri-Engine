# Makefile for NeoShinri Engine

.PHONY: test coverage clean

# Run tests with coverage and show missing lines
coverage:
	PYTHONPATH=. pytest --cov=neoshinri --cov-report=term-missing

# Run tests only (no coverage)
test:
	PYTHONPATH=. pytest

# Remove coverage and pytest cache files
clean:
	rm -rf .pytest_cache .coverage htmlcov
