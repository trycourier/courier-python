# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/trycourier/courier-python.

## Local development

- Fork this repository
- Clone your fork
- Install virtualenv: `pip install virtualenv`
- Run `make install`
- Run `source env/bin/activate`
- Write code!
- When finished, run `deactivate` to stop using this environment.

## Releasing New Versions

To put courier-python on PyPI

- Ensure you have maintainer privileges in PyPI
- Update your `~/.pypirc` if necessary to contain your username and password (hint: you can run `python setup.py register`)
- Run `make release`, which will create the dists and upload them to PyPI
- Confirm you are able to successfully install the new version by running `pip install trycourier`
