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
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of notifications. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results and paging info
        """
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def getContent(self, notification_id):
        """
        Get the notification content

        Args:
            notification_id (str): A unique identifier associated with
            the notification

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains notification content
        """
        url = "%s/%s/content" % (self.uri, notification_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def getDraftContent(self, notification_id):
        """
        Get the notification draft content

        Args:
            notification_id (str): A unique identifier associated with
            the notification

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains notification draft content
        """
        url = "%s/%s/draft/content" % (self.uri, notification_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def postVariations(self, notification_id, blocks, channels=None):
        """
        Post the notification variations

        Args:
            notification_id (str): A unique identifier associated with
            the notification
            blocks (list): Variation Blocks
            channels (list, optional): Variation Channels

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/variations" % (self.uri, notification_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.post(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def postDraftVariations(self, notification_id, blocks, channels=None):
        """
        Post the notification draft variations

        Args:
            notification_id (str): A unique identifier associated with
            the notification
            blocks (list): Variation Blocks
            channels (list, optional): Variation Channels

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/draft/variations" % (self.uri, notification_id)
        payload = {
            'blocks': blocks,
            'channels': channels
        }

        resp = self.session.post(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def getSubmissionChecks(self, notification_id, submission_id):
        """
        Get the notification submission checks

        Args:
            notification_id (str): A unique identifier associated with
            the notification
            submission_id (str): A unique identifier associated with
            the submission

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains notification submission checks
        """
        url = "%s/%s/%s/checks" % (self.uri, notification_id, submission_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def putSubmissionChecks(self, notification_id, submission_id, checks):
        """
        Post the notification submission checks

        Args:
            notification_id (str): A unique identifier associated with
            the notification
            submission_id (str): A unique identifier associated with
            the submission
            checks (list): A list of checks

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains notification submission checks
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

    def deleteSubmissionChecks(self, notification_id, submission_id):
        """
        Delete the notification submission checks

        Args:
            notification_id (str): A unique identifier associated with
            the notification
            submission_id (str): A unique identifier associated with
            the submission

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s/%s/checks" % (self.uri, notification_id, submission_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)
