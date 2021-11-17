from .exceptions import CourierAPIException


class Notifications():
    key = "notifications"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def list(self, cursor=None):
        """
        Get the list of notifications

        Args::
            - cursor (str, optional): A unique identifier that allows for
            - fetching the next set of notifications. Defaults to None.

        Raises:
            - CourierAPIException: Any error returned by the Courier API

        Returns:
            - dict: Contains results and paging info
        """
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_content(self, notification_id):
        """
        Get the notification content

        Args:
            - notification_id (str): A unique identifier associated with
            the notification

        Raises:
            - CourierAPIException: Any error returned by the Courier API

        Returns:
            - dict: Contains notification content
        """
        url = "%s/%s/content" % (self.uri, notification_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_draft_content(self, notification_id):
        """
        Get the notification draft content

        Args:
            - notification_id (str): A unique identifier associated with
            the notification

        Raises:
            - CourierAPIException: Any error returned by the Courier API

        Returns:
            - dict: Contains notification draft content
        """
        url = "%s/%s/draft/content" % (self.uri, notification_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_locales(self, notification_id, blocks, channels=None):
        """
        Put notification locales

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - blocks (list): Locale Blocks
            - channels (list, optional): Locale Channels

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/locales" % (self.uri, notification_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def put_draft_locales(self, notification_id, blocks, channels=None):
        """
        Put notification draft locales

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - blocks (list): Locale Blocks
            - channels (list, optional): Locale Channels

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/draft/locales" % (self.uri, notification_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def put_locale(self, notification_id, locale_id, blocks, channels=None):
        """
        Put notification locale

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - locale_id (str): A  unique identifier associated with the locale
            - blocks (list): Locale Blocks
            - channels (list, optional): Locale Channels

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/locales/%s" % (self.uri, notification_id, locale_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def put_draft_locale(self, notification_id, locale_id, blocks,
                         channels=None):
        """
        Put notification draft locale

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - locale_id (str): A  unique identifier associated with the locale
            - blocks (list): Locale Blocks
            - channels (list, optional): Locale Channels

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/draft/locales/%s" % (self.uri, notification_id, locale_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def post_block_locales(self, notification_id, block_id, block_locales):
        """
        Post notification block locales

        Args:
            - notification_id (str): A unique identifier associated with
            - the notification
            - locale_id (str): A  unique identifier associated with the locale
            - block_locales (dict): Block locales where key is locale_id and
            value is str or { "parent"?: str, "children"?: str }

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/blocks/%s/locales" % (self.uri, notification_id, block_id)

        resp = self.session.post(url, json=block_locales)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def post_draft_block_locales(self, notification_id,
                                 block_id, block_locales):
        """
        Post draft notification block locales

        Args:
            - notification_id (str): A unique identifier associated with
            - the notification
            - locale_id (str): A  unique identifier associated with the locale
            - block_locales (dict): Block locales where key is locale_id and
            value is str or { "parent"?: str, "children"?: str }

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/draft/blocks/%s/locales" % (
            self.uri, notification_id, block_id)

        resp = self.session.post(url, json=block_locales)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def post_channel_locales(self, notification_id,
                             channel_id, channel_locales):
        """
        Post notification channel locales

        Args:
            - notification_id (str): A unique identifier associated with
            - the notification
            - locale_id (str): A  unique identifier associated with the locale
            - channel_locales (dict): Channel locales where key is locale_id
            and value is str

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/channels/%s/locales" % (self.uri,
                                             notification_id, channel_id)

        resp = self.session.post(url, json=channel_locales)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def post_draft_channel_locales(self, notification_id,
                                   channel_id, channel_locales):
        """
        Post draft notification channel locales

        Args:
            - notification_id (str): A unique identifier associated with
            - the notification
            - locale_id (str): A  unique identifier associated with the locale
            - channel_locales (dict): Channel locales where key is locale_id
            and value is str

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/draft/channels/%s/locales" % (self.uri,
                                                   notification_id, channel_id)

        resp = self.session.post(url, json=channel_locales)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def get_submission_checks(self, notification_id, submission_id):
        """
        Get the notification submission checks

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - submission_id (str): A unique identifier associated with
            the submission

        Raises:
            - CourierAPIException: Any error returned by the Courier API

        Returns:
            - dict: Contains notification submission checks
        """
        url = "%s/%s/%s/checks" % (self.uri, notification_id, submission_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_submission_checks(self, notification_id, submission_id, checks):
        """
        Post the notification submission checks

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - submission_id (str): A unique identifier associated with
            the submission
            - checks (list): A list of checks

        Raises:
            - CourierAPIException: Any error returned by the Courier API

        Returns:
            - dict: Contains notification submission checks
        """
        url = "%s/%s/%s/checks" % (self.uri, notification_id, submission_id)

        headers = {}

        payload = {
            'checks': checks
        }

        resp = self.session.put(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def delete_submission_checks(self, notification_id, submission_id):
        """
        Delete the notification submission checks

        Args:
            - notification_id (str): A unique identifier associated with
            the notification
            - submission_id (str): A unique identifier associated with
            the submission

        Raises:
            - CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/%s/checks" % (self.uri, notification_id, submission_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)
