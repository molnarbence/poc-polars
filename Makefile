install:
	uv pip install -r requirements.txt

install-dev:
	uv pip install -r requirements-dev.txt
	uv pip install -e .

freeze:
	UV_CUSTOM_COMPILE_COMMAND="make freeze" uv pip compile --output-file requirements.txt pyproject.toml
	UV_CUSTOM_COMPILE_COMMAND="make freeze" uv pip compile --output-file requirements-dev.txt --extra=dev pyproject.toml

freeze-upgrade:
	UV_CUSTOM_COMPILE_COMMAND="make freeze-upgrade" uv pip compile --upgrade --output-file requirements.txt pyproject.toml
	UV_CUSTOM_COMPILE_COMMAND="make freeze-upgrade" uv pip compile --upgrade --extra=dev --output-file requirements-dev.txt pyproject.toml

format:
	ruff format .

test:
	ruff check .
	mypy .
	pytest

run:
	python app/main.py