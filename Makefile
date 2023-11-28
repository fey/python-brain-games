python-version:
	which python
	python --version

brain-games:
	poetry run python -m brain_games.scripts.brain_games

install:
	poetry install

lint:
	poetry run flake8 .
