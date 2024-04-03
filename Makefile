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

make lint:
	poetry run flake8 gendiff
