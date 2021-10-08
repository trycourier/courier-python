all: clean venv install

venv:
				virtualenv env

install: venv
				. env/bin/activate; pip install -r dev-requirements.txt
				. env/bin/activate; pip install -e .

analysis:
				. env/bin/activate; flake8 trycourier

test: analysis
				. env/bin/activate; py.test --cov-report term-missing --cov-report html --cov trycourier tests/

build: install
				. env/bin/activate; python setup.py sdist
				. env/bin/activate; python setup.py bdist_wheel

release: build; twine upload -r pypi dist/*

release-test: build; twine upload -r test dist/*

clean:
				rm -rf env build dist *.egg-info
