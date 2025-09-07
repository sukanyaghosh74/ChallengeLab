# ChallengeLab Makefile

.PHONY: help install test clean build docker-test lint format

help: ## Show this help message
	@echo "ChallengeLab - Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install ChallengeLab in development mode
	pip install -e .

install-deps: ## Install dependencies
	pip install -r requirements.txt

test: ## Run all tests
	@echo "Testing all challenges..."
	@for challenge in $$(challengelab list | grep "  -" | sed 's/  - //'); do \
		echo "Testing challenge: $$challenge"; \
		challengelab test "$$challenge" || exit 1; \
	done

test-reverse-string: ## Test reverse-string challenge
	challengelab test reverse-string

run-reverse-string: ## Run reverse-string challenge
	echo "hello world" | challengelab run reverse-string --input "hello world"

docker-test: ## Test using Docker Compose
	docker-compose up --build --abort-on-container-exit reverse-string

build-docker: ## Build Docker images for all challenges
	@for challenge in $$(challengelab list | grep "  -" | sed 's/  - //'); do \
		echo "Building Docker image for: $$challenge"; \
		docker build -f docker/Dockerfile.base -t challengelab-$$challenge:latest ./challenges/$$challenge || exit 1; \
	done

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint: ## Run linting
	flake8 challenge_manager/
	pylint challenge_manager/

format: ## Format code
	black challenge_manager/
	isort challenge_manager/

init-challenge: ## Create a new challenge (usage: make init-challenge NAME=my-challenge)
	@if [ -z "$(NAME)" ]; then \
		echo "Usage: make init-challenge NAME=my-challenge"; \
		exit 1; \
	fi
	challengelab init $(NAME) --description "A new challenge"

list: ## List all challenges
	challengelab list

ci: ## Run CI pipeline locally
	@echo "Running CI pipeline..."
	@echo "1. Installing dependencies..."
	pip install -r requirements.txt
	pip install -e .
	@echo "2. Building Docker images..."
	$(MAKE) build-docker
	@echo "3. Running tests..."
	$(MAKE) test
	@echo "4. Testing with Docker Compose..."
	$(MAKE) docker-test
	@echo "CI pipeline completed successfully!"
