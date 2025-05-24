install:
	uv sync --frozen

upgrade:
	uv lock --upgrade

lint:
	uv run ruff check
	uv run mypy

format:
	uv run ruff format

test:
	uv run ruff check
	uv run mypy .
	pytest



run:
	uv run main.py

clean:
	rm -f ./outputs/*.parquet
	rm -f ./outputs/*.csv
