# Makefile
install: # инициализация
	poetry install

build: # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета
	python3 -m pip install --user dist/*.whl

brain-games: # запуск программы
	poetry run brain-games
