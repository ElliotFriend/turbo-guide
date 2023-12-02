.PHONY: lint

lint:
	@echo ♻️ Reformatting Code
	poetry run black .
	@echo ✅  Style Checks with PyLint
	poetry run pylint ./01/*.py
	@echo 🧪 Type Checks with MyPy
	poetry run mypy 01/
