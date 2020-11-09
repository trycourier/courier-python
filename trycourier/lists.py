from .exceptions import CourierAPIException


class Lists():
    key = "lists"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def send(self,
             event,
             list=None,
             pattern=None,
             data={},
             brand=None,
             override=None,
             idempotency_key=None):
        """
        Send a notification to list(s) subscribers

        Args:
            event (str): A unique identifier that can be mapped to an
            individual Notification.
            list (str, optional): The list id intended to send. Defaults to
            None. list or pattern required.
            pattern (str, optional): The pattern used to identify list(s)
            intended to send. Defaults to None. list or pattern required.
            data (dict, optional): An object that includes any data you want to
            pass to a message template. Defaults to {}.
            brand (str, optional): A unique identifier that represents the
            brand that should be used for rendering the notification. Defaults
            to None.
            override (dict, optional): An object that is merged into the
            request sent by Courier to the provider to override properties or
            to gain access to features in the provider API that are not
            natively supported by Courier. Defaults to None.
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.

        Raises:
            Exception: Missing list or pattern
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a messageId
        """

        if (not list and not pattern) or (list and pattern):
            raise Exception('list.send requires a list id or a pattern')

        url = "%s/send/list" % self.base_url
        headers = {}
        payload = {
            'event': event,
            'data': data
        }

        if list:
            payload['list'] = list

        if pattern:
            payload['pattern'] = pattern

        if brand:
            payload['brand'] = brand

        if override:
            payload['override'] = override

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def list(self, cursor=None, pattern=None):
        """
        Get the list of lists

        Args:
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of brands. Defaults to None.
            pattern (str, optional): A pattern used to filter the list items
            returned. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains items and paging info
        """
        params = {}

        if cursor:
            params['cursor'] = cursor

        if pattern:
            params['pattern'] = pattern

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get(self, list_id):
        """
        Get the list items.

        Args:
            list_id (str): A unique identifier associated with the list you
            wish to retrieve.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains list item
        """
        url = "%s/%s" % (self.uri, list_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put(self, list_id, name):
        """
        Create or replace an existing list with the supplied values.

        Args:
            list_id (str): A unique identifier associated with the list you
            wish to create or update.
            name (str): List name.

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s" % (self.uri, list_id)
        payload = {
            'name': name
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def delete(self, list_id):
        """
        Delete a list by list ID.

        Args:
            list_id (str): A unique identifier associated with the list you
            wish to create or update.

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s" % (self.uri, list_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def restore(self, list_id):
        """
        Restore an existing list.

        Args:
            list_id (str): A unique identifier associated with the list you
            wish to create or update.

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/restore" % (self.uri, list_id)

        resp = self.session.put(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def get_subscriptions(self, list_id, cursor=None):
        """
        Get the list's subscriptions.

        Args:
            list_id (str): A unique identifier associated with the list from
            which you wish to retrieve subscriptions.
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of list subscriptions. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains items and paging info
        """
        url = "%s/%s/subscriptions" % (self.uri, list_id)
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_subscriptions(self, list_id, recipients):
        """
        Subscribe multiple recipients to a list.
        (note: if the List does not exist, it will be automatically created)

        Args:
            list_id (str): A unique identifier associated with the list.
            recipients (list): List of recipient subscriptions.

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/subscriptions" % (self.uri, list_id)
        payload = {
            'recipients': recipients
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def subscribe(self, list_id, recipient_id):
        """
        Subscribe a recipient to an existing list.
        (note: if the List does not exist, it will be automatically created)

        Args:
            list_id (str): A unique identifier representing the list id.
            recipient_id (str): A unique identifier representing the recipient
            associated with the list

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/subscriptions/%s" % (self.uri, list_id, recipient_id)

        resp = self.session.put(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def unsubscribe(self, list_id, recipient_id):
        """
        Delete a subscription to a list by list and recipient ID.

        Args:
            list_id (str): A unique identifier representing the list id.
            recipient_id (str): A unique identifier representing the recipient
            associated with the list

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/subscriptions/%s" % (self.uri, list_id, recipient_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def find_by_recipient_id(self, recipient_id, cursor=None):
        """
        Returns the subscribed lists for a specified recipient Profile.

        Args:
            recipient_id (str): A unique identifier representing the recipient
            associated with the requested profile.
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of list subscriptions. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results and paging info
        """
        url = "%s/profiles/%s/lists" % (self.base_url, recipient_id)
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
