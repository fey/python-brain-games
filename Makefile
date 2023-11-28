python-version:
	which python
	python --version

brain-games:
	poetry run python -m brain_games.scripts.brain_games

brain-even:
	poetry run python -m brain_games.scripts.brain_even

brain-calc:
	poetry run python -m brain_games.scripts.brain_calc

brain-gcd:
	poetry run python -m brain_games.scripts.brain_gcd

install:
	poetry install

lint:
	poetry run flake8 .

build:
	rm -rf dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
