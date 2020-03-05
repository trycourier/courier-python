from os import environ
from urllib.parse import urljoin

from .exceptions import CourierAPIException
from .session import CourierAPISession

__version__ = '1.0.0'


class Courier(object):

    def __init__(self,
                 base_url='https://api.trycourier.app',
                 auth_token=None,
                 username=None,
                 password=None):
        """
        Instantiate a new API client.
        Args:
          host (str): Hostname of courier instance.
          auth_token (str): Auth Token used for Token Auth
          username (str): Username used for Basic Auth
          password (str): Password used for Basic Auth
        """
        self.base_url = base_url

        # Initialize the session.
        self.session = CourierAPISession()
        self.session.init_library_version(__version__)

        # Pass auth creds to the session
        if username and password:
            self.session.init_basic_auth(username, password)

        # Check environment variable for auth Key
        if not auth_token:
            auth_token = environ.get('COURIER_AUTH_TOKEN', None)

        if auth_token:
            self.session.init_token_auth(auth_token)

    # Perform an API request
    def send(self,
             event,
             recipient,
             data={},
             profile=None,
             preferences=None,
             override=None):
        """
        Send a notification for the provided event to the provided recipient
        """
        url = urljoin(self.base_url, "send")
        payload = {
            'event': event,
            'recipient': recipient,
            'data': data
        }
        if profile:
            payload['profile'] = profile

        if preferences:
            payload['preferences'] = preferences

        if override:
            payload['override'] = override

        resp = self.session.post(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
