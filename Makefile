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

# =============================================SPHINX============================================= 
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= docs/sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

# Put it first so that "make" without argument is like "make help".
.PHONY: help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.PHONY: Makefile
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# =============================================SPHINX=============================================
