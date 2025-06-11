# Makefile for NeoShinri Engine

.PHONY: test coverage clean

# Install dependencies
install:
	pip install -r requirements.txt

# Format code using black
format:
	black neoshinri tests

# Run controller entrypoint
run-controller:
	uvicorn neoshinri.controller.main:app --port 8001 --reload

# Run transport tunnel entrypoint
run-tunnel:
	uvicorn neoshinri.transport.main:app --port 8000 --reload

# Run both controller and tunnel in a tmux session
dev:
	@echo "Starting Controller and Tunnel..."
	@tmux new-session -d -s neo 'make run-controller' \; split-window -h 'make run-tunnel' \; attach

# Check ACP message serialization
check-acp:
	python -c "from neoshinri.shared.protocols.acp import ACPMessage; print(ACPMessage(sender='cli', receiver='agent', message_type='command', content='test').to_json())"
	
# Run tests with coverage and show missing lines
coverage:
	PYTHONPATH=. pytest --cov=neoshinri --cov-report=term-missing

# Run tests only (no coverage)
test:
	PYTHONPATH=. pytest

# Lint code using ruff
lint:
	ruff check neoshinri tests

# Remove coverage and pytest cache files
clean:
	rm -rf .ruff_cache .pytest_cache .coverage htmlcov
