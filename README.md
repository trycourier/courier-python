# `trycourier`

This Python Package helps you send notifications through [Courier](https://www.courier.com/), the smartest way to design &amp; deliver notifications. Design your notifications once using our drag &amp; drop editor, then deliver to any channel through one API. Email, mobile push, SMS, Slack &mdash; you name it!

## Installation

Install from PyPI using [pip](http://www.pip-installer.org/en/latest/):

```shell
$ pip install trycourier
```

Python 3.5 or later is required.

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

### Timeouts

As of v1.4.0, the timeout is defaulted to 5 seconds. This is configurable using the `timeout` parameter when creating a client. You can specify the time in seconds using a `float` value for both Connect and Read or use a tuple to set them for each individual one `(Connect, Read)`.

```python
client = Courier(auth_token="your-auth-token",
                 timeout=3.5)

client = Courier(auth_token="your-auth-token",
                 timeout=(3.2, 3.3))
```

## Advanced Usage

```python
from trycourier import Courier

client = Courier(auth_token="your-auth-token")

"""
Example: send a message to a recipient
"""
resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={}, # optional
    brand="your-brand-id", # optional
    data={}, # optional
    preferences={}, # optional
    override={} # optional
)
print(resp['messageId'])

"""
Example: send a message to a list
"""
resp = client.lists.send(
  event="your-event-id",
  list="your.list.id",
  brand="your-brand-id", # optional
  data={}, # optional
  override={} # optional
)
print(resp['messageId'])

"""
Example: send a message to a list pattern
"""
resp = client.lists.send(
  event="your-event-id",
  pattern="your.list.*",
  brand="your-brand-id", # optional
  data={}, # optional
  override={} # optional
)
print(resp['messageId'])

"""
Example: create a recipient's profile
"""
resp = client.profile.add(
  recipient_id,
  {
    "email":"example@example.com",
    "name":"Example Name"
  }
)

Example: replace or create a recipient's profile
"""
resp = client.profile.replace(
  recipient_id,
  {
    "email": "example@example.com"
  }
)
print(resp['status'])

"""
Example: merge or create a recipient's profile
"""
resp = client.profile.merge(
  recipient_id,
  {
    "phone_number": "+15555555555"
  }
)
print(resp['status'])

"""
Example: get the subscribed lists of a recipient
"""
resp = client.profile.get_subscriptions(
  recipient_id,
  cursor #optional
)
print(resp)

"""
Example: edit the contents of a recipient's profile with a patch operation 
(follows JSON Patch conventions: RFC 6902). 
"""
resp = client.profile.patch(
  recipient_id,
  [
    { 
      "op": "add", #operation 1: add this email to profile
      "path": "/parent",
      "value": "example@example.com"
    }
    {
      "op": "replace", #operation 2: update with new email
      "path": "/parent",
      "value": "jane@doe.com"
    }
    {
      "op": "copy", #operation 3: copy that email to /emergency_contact
      "from": "/parent",
      "path": "/emergency_contact"
    }
    ...
  ]
)
print(resp)


"""
Example: get a recipient's profile
"""
resp = client.profile.get(recipient_id)
print(resp)


"""
Example: fetch the statuses of messages you've previously sent.
"""
resp = client.messages.list(
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
  event="your-event-id", # optional
  list="your-list-id, #optional
  message_id="your-message-id" #optional
  notification=["message-status-1", "message-status-2",...] #optional
  recipient="recipient-id" # optional
)
print(resp)

"""
Example: fetch the status of a message you've previously sent
"""
resp = client.messages.get(message_id)
print(resp)

"""
Example: fetch the array of events of a message you've previously sent.
"""
resp = client.messages.get_history(
message_id="your-message-id",
type="list-type" #optional ("FILTERED", "RENDERED", "MAPPED", "PROFILE_LOADED")
)
print(resp)

"""
Example: fetch the list of events
"""
resp = client.get_events()
print(resp)

"""
Example: fetch a specific event by event ID
"""
resp = client.get_event(event_id)
print(resp)

"""
Example: create or replace an event
"""
resp = client.replace_event(
  event_id,
  notification_id="GRPVB5P0BHMEZSNY6TP2X7TQHEBF",
  type="notificaton" ## optional, defaults to notification
)
print(resp)

"""
Example: get all brands
"""
resp = client.get_brands(
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
)
print(resp)

"""
Example: get a specific brand
"""
resp = client.get_brand(brand_id)
print(resp)

"""
Example: create a brand
"""
resp = client.create_brand({
  name="My Brand",
  settings={
    "color": {
      "primary": "#0000FF",
      "secondary": "#FF0000",
      "tertiary": "#00FF00"
    }
  }
})
print resp

"""
Example: replace a brand
"""
resp = client.replace_brand(
  brand_id,
  name="My New Brand",
  settings={
    "color": {
      "primary": "#FF0000",
      "secondary": "#00FF00",
      "tertiary": "#0000FF"
    }
  }
)
print resp

"""
Example: delete a brand
"""
client.delete_brand(brand_id)

"""
Example: get all lists
"""
resp = client.lists.list(
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
)
print resp

"""
Example: get a specific list
"""
resp = client.lists.get(list_id)
print resp

"""
Example: create or replace a list
"""
client.lists.put(list_id, name="My List")

"""
Example: delete a list
"""
client.lists.delete(list_id)

"""
Example: restore a list
"""
client.lists.restore(list_id)

"""
Example: get a list's subscribptions
"""
resp = client.lists.get_subscriptions(list_id,
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
)
print resp

"""
Example: replace many recipients to a new or existing list
"""
client.lists.put_subscriptions(list_id, [
  "RECIPIENT_ID_1",
  "RECIPIENT_ID_2"
])

"""
Example: Example: subscribe single recipient to a new or existing list
"""
client.lists.subscribe(list_id, recipient_id)

"""
Example: unsubscribe recipient from list
"""
client.lists.unsubscribe(list_id, recipient_id)

"""
Example: get a recipient's subscribed lists
"""
resp = client.lists.find_by_recipient_id(recipient_id,
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
)
print resp

```

### Idempotency

For `POST` methods, you can supply an `idempotency_key` to ensure the idempotency of the API Call. We recommend that you use a `V4 UUID` for the key. Keys are eligible to be removed from the system after they're at least 24 hours old, and a new request is generated if a key is reused after the original has been removed.

```python
import uuid
from trycourier import Courier

client = Courier()

idempotency_key = uuid.uuid4()

resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={
        "email": "example@example.com",
        "phone_number": "555-867-5309"
    },
    data={
      "world": "Python!"
    },
    idempotency_key=idempotency_key
)
print(resp['messageId'])
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/trycourier/courier-python. See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
