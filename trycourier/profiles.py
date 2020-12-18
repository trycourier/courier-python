from .exceptions import CourierAPIException


class Profiles():
    key = "profiles"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def get(self, recipient_id):
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

        url = "%s/%s" % (self.uri, recipient_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_subscriptions(self, recipient_id, cursor=None):
        """
        Returns the subscribed lists stored for a specified recipient.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of list subscriptions

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """
        params = {}
        if cursor:
            params['cursor'] = cursor
        url = "%s/%s/lists" % (self.uri, recipient_id)
        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def add(self, recipient_id, profile):
        """
        Simply a wrapper for replace() for those who want to add a new profile
        """
        return self.replace(recipient_id, profile)

    def replace(self, recipient_id, profile):
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
        url = "%s/%s" % (self.uri, recipient_id)
        payload = {
            'profile': profile
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def merge(self, recipient_id, profile, idempotency_key=None):
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
        url = "%s/%s" % (self.uri, recipient_id)
        headers = {}
        payload = {
            'profile': profile
        }

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def patch(self, recipient_id, operations):
        """
        Apply a JSON Patch (RFC 6902) to the specified profile or create one
        if a profile doesn't already exist.

        Args:
            recipient_id (str): A unique identifier representing the
            recipient associated with the requested profile.
            operations[]: A list of patch operations to apply to
            the specified recipient.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a success
        """

        url = "%s/%s" % (self.uri, recipient_id)
        payload = {
            "patch": operations
        }
        resp = self.session.patch(url, json=payload)
        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
