docs:
	./scripts/generate_docs.sh

serve:
	mkdocs serve

build:
	mkdocs build

docs-serve:
	./scripts/generate_docs.sh
	mkdocs serve

clean:
	rm -rf site
