from os import environ

from .audiences import Audiences
from .audit_events import AuditEvents
from .automations import Automations
from .bulk import Bulk
from .exceptions import CourierAPIException
from .session import CourierAPISession
from .lists import Lists
from .messages import Messages
from .notifications import Notifications
from .profiles import Profiles

__version__ = '4.4.0'


class Courier(object):

    def __init__(self,
                 base_url=None,
                 auth_token=None,
                 username=None,
                 password=None,
                 timeout=5):
        """
        Instantiate a new API client.
        Args:
          host (str): Hostname of Courier instance.
          auth_token (str): Auth Token used for Token Auth
          username (str): Username used for Basic Auth
          password (str): Password used for Basic Auth
          timeout (float|tuple): Timeout in seconds. (Connect, Read) Defaults
          to 5 seconds for both.
        """
        if base_url:
            self.base_url = base_url

        else:
            default_url = "https://api.courier.com"
            self.base_url = environ.get('COURIER_BASE_URL', default_url)

        # Initialize the session.
        self.session = CourierAPISession(timeout)
        self.session.init_library_version(__version__)

        # Token Auth takes precedence
        if auth_token:
            self.session.init_token_auth(auth_token)
        elif 'COURIER_AUTH_TOKEN' in environ:
            self.session.init_token_auth(environ['COURIER_AUTH_TOKEN'])

        # If no token auth, then Basic Auth
        elif username and password:
            self.session.init_basic_auth(username, password)
        elif 'COURIER_AUTH_USERNAME' in environ \
                and 'COURIER_AUTH_PASSWORD' in environ:
            username = environ.get('COURIER_AUTH_USERNAME', None)
            password = environ.get('COURIER_AUTH_PASSWORD', None)
            self.session.init_basic_auth(username, password)

        self.audiences = Audiences(self.base_url, self.session)
        self.audit_events = AuditEvents(self.base_url, self.session)
        self.automations = Automations(self.base_url, self.session)
        self.bulk = Bulk(self.base_url, self.session)
        self.lists = Lists(self.base_url, self.session)
        self.messages = Messages(self.base_url, self.session)
        self.notifications = Notifications(self.base_url, self.session)
        self.profiles = Profiles(self.base_url, self.session)

    # Perform an API request
    def send(self,
             event,
             recipient,
             data={},
             profile=None,
             brand=None,
             preferences=None,
             override=None,
             idempotency_key=None,
             idempotency_expiration=None):
        """
        Send a notification for the provided event to the provided recipient.

        Args:
            event (str): A unique identifier that can be mapped to an
            individual Notification.
            recipient (str): A unique identifier associated with the
            recipient of the delivered message.
            data (dict, optional): An object that includes any data you want to
            pass to a message template. Defaults to {}.
            profile (dict, optional): Any key-value pairs required by your
            chosen Integrations. Defaults to None.
            brand (str, optional): A unique identifier that represents the
            brand that should be used for rendering the notification.
            preferences (dict, optional): Any preferences for the recipient.
            Defaults to None.
            override (dict, optional): An object that is merged into the
            request sent by Courier to the provider to override properties or
            to gain access to features in the provider API that are not
            natively supported by Courier. Defaults to None.
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a messageId
        """

        url = "%s/%s" % (self.base_url, "send")
        headers = {}
        payload = {
            'event': event,
            'recipient': recipient,
            'data': data
        }
        if profile:
            payload['profile'] = profile

        if brand:
            payload['brand'] = brand

        if preferences:
            payload['preferences'] = preferences

        if override:
            payload['override'] = override

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def send_message(self,
                     message,
                     idempotency_key=None,
                     idempotency_expiration=None):
        """
        Send a message based on its configuration

        Args:
            message (dict): An object that the message you want to send.
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.
            idempotency_expiration (str, optional): A unique identifier used to
            ensure idempotency of the the request. Passed in the
            x-idempotency-expiration HTTP header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a requestId
        """

        url = "%s/%s" % (self.base_url, "send")
        headers = {}
        payload = {
            'message': message
        }

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

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

    def merge_profile(self,
                      recipient_id,
                      profile,
                      idempotency_key=None,
                      idempotency_expiration=None):
        """
        Merge the supplied values with an existing profile or create a new
        profile if one doesn't already exist.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.
            profile (dict): Key-value pairs required by your chosen
            Integrations.
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """

        url = "%s/%s/%s" % (self.base_url, "profiles", recipient_id)
        headers = {}
        payload = {
            'profile': profile
        }

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_messages(self, cursor=None, recipient=None):
        """
        Fetch the statuses of messages you've previously sent.

        Args:
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of message statuses. Defaults to None.
            recipient (str, optional): A unique identifier representing the
            recipient to filter the returned messages. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results and paging info
        """

        url = "%s/%s" % (self.base_url, "messages")
        params = {}

        if cursor:
            params['cursor'] = cursor

        if recipient:
            params['recipient'] = recipient

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_message(self, message_id):
        """
        Get the status of the message corresponding to message_id.

        Args:
            message_id (str): A unique identifier representing the
            message associated with the requested message.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success, as well as details
        """

        url = "%s/%s/%s" % (self.base_url, "messages", message_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_events(self):
        """
        Fetch the list of events.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results
        """
        url = "%s/%s" % (self.base_url, "events")

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_event(self, event_id):
        """
        Fetch a specific event by event ID.

        Args:
            event_id (str): A unique identifier associated with the event you
            wish to retrieve.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results
        """
        url = "%s/%s/%s" % (self.base_url, "events", event_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def replace_event(self, event_id, notification_id, type="notification"):
        """
        Replace an existing event map the supplied values or create a new event
        map if one does not already exist.

        Args:
            event_id (str): A unique identifier associated with the event you
            wish to update.
            notification_id (str): The ID of the notification this event
            maps to.
            type (str, optional): The type of event map. Defaults to
            "notification".

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/%s" % (self.base_url, "events", event_id)
        payload = {
            'id': notification_id,
            'type': type
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_brands(self, cursor=None):
        """
        Get the list of brands

        Args:
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of brands. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results and paging info
        """
        url = "%s/%s" % (self.base_url, "brands")
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_brand(self, brand_id):
        """
        Fetch a specific brand by brand ID.

        Args:
            brand_id (str): A unique identifier associated with the brand you
            wish to retrieve.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains result
        """
        url = "%s/%s/%s" % (self.base_url, "brands", brand_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def create_brand(self,
                     name,
                     settings,
                     id=None,
                     snippets=None,
                     idempotency_key=None,
                     idempotency_expiration=None):
        """
        Create a new brand

        Args:
            name (str): Brand name
            settings (dict): Brand colors and Email settings
            id (str, optional): Brand identifier. Defaults to None.
            snippets (dict, optional): Reusable handlebars templates that can
            be used in your notifications. Defaults to None.
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains resulting brand
        """

        url = "%s/%s" % (self.base_url, "brands")
        headers = {}
        payload = {
            'name': name,
            'settings': settings
        }

        if id:
            payload['id'] = id

        if snippets:
            payload['snippets'] = snippets

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def replace_brand(self,
                      brand_id,
                      name,
                      settings,
                      snippets=None):
        """
        Replace an existing brand with the supplied values.

        Args:
            brand_id (str): A unique identifier associated with the brand you
            wish to update.
            name (str): Brand name
            settings (dict): Brand colors and Email settings
            snippets (dict, optional): Reusable handlebars templates that can
            be used in your notifications. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains resulting brand
        """

        url = "%s/%s/%s" % (self.base_url, "brands", brand_id)
        payload = {
            'name': name,
            'settings': settings
        }

        if snippets:
            payload['snippets'] = snippets

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def delete_brand(self, brand_id):
        """
        Delete a brand by brand ID.

        Args:
            brand_id (str): A unique identifier associated with the brand you
            wish to delete.

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """

        url = "%s/%s/%s" % (self.base_url, "brands", brand_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)
