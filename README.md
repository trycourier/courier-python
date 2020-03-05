# `trycourier`

This Python Package helps you send notifications through [Courier](https://www.trycourier.com/), the smartest way to design &amp; deliver notifications. Design your notifications once using our drag &amp; drop editor, then deliver to any channel through one API. Email, mobile push, SMS, Slack &mdash; you name it!

## Installation

Install from PyPI using [pip](http://www.pip-installer.org/en/latest/):

```shell
$ pip install trycourier
```

Python 2.7 or later is required.

## Usage

### Using Token Auth

```python
from trycourier import Courier

client = Courier(auth_token="your-auth-token") #or set via COURIER_AUTH_TOKEN env var

resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={
        "email": "example@example.com",
        "phone_number": "555-867-5309"
    },
    data={
      "world": "Python!"
    }
)
print(resp['messageId'])
```

### Using Basic Auth

```python
from trycourier import Courier

client = Courier(username="your-username", password="your-password")

resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={
        "email": "example@example.com",
        "phone_number": "555-867-5309"
    },
    data={
      "world": "Python!"
    }
)
print(resp['messageId'])
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/trycourier/courier-python.

### Local development

- Fork this repository
- Clone your fork
- Install virtualenv: `pip install virtualenv`
- Run `make install`
- Run `source env/bin/activate`
- Write code!
- When finished, run `deactivate` to stop using this environment.

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
