# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/trycourier/courier-python.

## Local development

- Fork this repository
- Clone your fork
- Install virtualenv: `pip install virtualenv`
- Run `make install`
- Run `source env/bin/activate`
- Write code!
- Test your code using `make test`
- When finished, run `deactivate` to stop using this environment.

## Releasing New Versions

To put courier-python on PyPI

- Update the CHANGELOG.md
- Bump the package version in `setup.py` and `trycourier/client.py`
- Submit a PR to merge changes into master
- Ensure you have maintainer privileges in PyPI
- Create and push a new version tag

  ```bash
  git tag -a v<VERSION> -m v<VERSION>
  git push origin v<VERSION>
  ```

- Wait for GitHub Action to test and deploy
- Confirm you are able to successfully install the new version by running `pip install trycourier`
