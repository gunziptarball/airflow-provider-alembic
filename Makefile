test:
	pytest tests

pretty:
	isort --profile "black" . && black .