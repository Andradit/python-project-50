install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install --force dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/