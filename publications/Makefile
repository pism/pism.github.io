all: published.md submitted_papers.md

published.md: list_references.py applications.bib
	python3 $^ > $@

submitted_papers.md: list_references.py submitted.bib
	python3 $^ > $@
