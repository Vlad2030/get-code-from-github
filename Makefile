# ============================================VARIABLES===========================================
lib_directory = get_github_code
examples_directory = examples
code_directory = $(lib_directory) $(examples_directory)
# ============================================VARIABLES===========================================

# ==============================================CODE==============================================
.PHONY: lint
lint:
	isort --check-only $(code_directory)
	black --check --diff $(code_directory)
	ruff $(code_directory)
	mypy $(application_directory)

.PHONY: reformat
reformat:
	black $(code_directory)
	isort $(code_directory)
	ruff --fix $(code_directory)
# ==============================================CODE==============================================