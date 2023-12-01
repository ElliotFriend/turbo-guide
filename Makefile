.PHONY: lint

lint:
	@echo ♻️ Reformatting Code
	poetry run black .
	@echo ✅  Style Checks with PyLint
	poetry run pylint ./**/*.py
