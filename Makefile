.PHONY: lint

lint:
	@echo ♻️ Reformatting Code
	poetry run black .
	@echo ✅  Style Checks with PyLint
	poetry run pylint ./**/*.py
	@echo 🧪 Type Checks with MyPy
	poetry run mypy .
