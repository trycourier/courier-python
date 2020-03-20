from os import environ

from .exceptions import CourierAPIException
from .session import CourierAPISession

__version__ = '1.1.0'


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

        Args:
            event (str): A unique identifier that can be mapped to an
            individual Notification.
            recipient (str): A unique identifier associated with the
            recipient of the delivered message.
            data (dict, optional): An object that includes any data you want to
            pass to a message template. Defaults to {}.
            profile (dict, optional): Any key-value pairs required by your
            chosen Integrations. Defaults to None.
            preferences (dict, optional): Any preferences for the recipient.
            Defaults to None.
            override (dict, optional): An object that is merged into the
            request sent by Courier to the provider to override properties or
            to gain access to features in the provider API that are not
            natively supported by Courier. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a messageId
        """

        url = "%s/%s" % (self.base_url, "send")
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

    def get_profile(self, recipient_id):
        """
        Get the profile stored under the specified recipient ID.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """

        url = "%s/%s/%s" % (self.base_url, "profiles", recipient_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def replace_profile(self, recipient_id, profile):
        """
        Replace an existing profile with the supplied values or create a new
        profile if one does not already exist.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.
            profile (dict): Key-value pairs required by your chosen
            Integrations.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """
        url = "%s/%s/%s" % (self.base_url, "profiles", recipient_id)
        payload = {
            'profile': profile
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def merge_profile(self, recipient_id, profile):
        """
        Merge the supplied values with an existing profile or create a new
        profile if one doesn't already exist.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.
            profile (dict): Key-value pairs required by your chosen
            Integrations.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """

        url = "%s/%s/%s" % (self.base_url, "profiles", recipient_id)
        payload = {
            'profile': profile
        }

        resp = self.session.post(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
