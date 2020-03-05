all: clean venv install

venv:
				virtualenv env

install: venv
				. env/bin/activate; pip install -r dev-requirements.txt
				. env/bin/activate; pip install -e .

analysis:
				. env/bin/activate; flake8 trycourier

clean:
				rm -rf env build dist *.egg-info