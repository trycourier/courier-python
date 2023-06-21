from .exceptions import CourierAPIException


class Messages():
    key = "messages"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def list(self, cursor=None, event=None, list_id=None, message_id=None,
             notification=None, recipient=None):
        """
        Get the list of messages

        Args::
            cursor (str, optional): A unique identifier that allows for
            fetching the next set of brands. Defaults to None.
            event (str, optional): A unique identifier representing the
            event that was used to send the event. Defaults to None.
            list_id (str, optional): A unique identifier representing the
            list the message was sent to. Defaults to None.
            message_id (str, optional): A unique identifier representing
            the message_id returned from either /send or /send/list. Defaults
            to None.
            notification (str, optional): An indicator of the current status
            of the message. Multiple status values can be passed in. Defaults
            to None.
            recipient (str, optional): A unique identifier representing the
            recipient associated with the requested profile. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains items and paging info
        """
        params = {}

        if cursor:
            params['cursor'] = cursor
        if event:
            params['event'] = event
        if list_id:
            params['list'] = list_id
        if message_id:
            params['messageId'] = message_id
        if notification:
            params['notification'] = notification
        if recipient:
            params['recipient'] = recipient

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get(self, message_id):
        """
        Get the message items.

        Args:
            message_id (str): A unique identifier associated with the message
            you wish to retrieve (returned after each 'send()' call)

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains message item
        """
        url = "%s/%s" % (self.uri, message_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_history(self, message_id, type=None):
        """
        Get the message items.

        Args:
            message_id (str): A unique identifier associated with the message
            you wish to retrieve (returned after each 'send()' call)
            type (str, optional): A supported Message History type that will
            filter the events returned. Defaults to None.

        Raises:
                CourierAPIException: Any error returned by the Courier API

                Returns:
                    dict: Contains message item
                """
        params = {}
        if type:
            params['type'] = type

        url = "%s/%s/history" % (self.uri, message_id)

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def cancel(self, message_id):
        """
        Cancel the message delivery.

        Args:
            message_id (str): A unique identifier associated with the message
            you wish to retrieve (returned after each 'send()' call.
            See
            https://www.courier.com/docs/reference/send/message/#requestid-details
            for details.)

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains message item
        """
        url = "%s/%s/cancel" % (self.uri, message_id)

        resp = self.session.post(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
