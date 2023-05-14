# ============================================VARIABLES===========================================
LIBDIR			= get_github_code
EXAMPLSDIR		= examples
CODEDIR	= $(LIBDIR) $(EXAMPLSDIR)
SPHINXOPTS		?=
SPHINXBUILD		?= docs/sphinx-build
SOURCEDIR		= docs
BUILDDIR		= docs/_build
# ============================================VARIABLES===========================================

# ==============================================CODE==============================================
.PHONY: lint
lint:
	isort --check-only $(CODEDIR)
	black --check --diff $(CODEDIR)
	ruff $(CODEDIR)
	mypy $(application_directory)

.PHONY: reformat
reformat:
	black $(CODEDIR)
	isort $(CODEDIR)
	ruff --fix $(CODEDIR)
# ==============================================CODE==============================================

# =============================================SPHINX============================================= 
.PHONY: help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.PHONY: Makefile
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# =============================================SPHINX=============================================
