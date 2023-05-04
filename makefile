build:
	poetry build

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

# selfcheck:
#	poetry check

#test-coverage:
#	poetry run pytest --cov=page_analyzer --cov-report xml -vv

lint:
	poetry run flake8 task_manager

# check: selfcheck lint

schema-load:
	psql taskdb < database.sql

start:
	python3 manage.py runserver