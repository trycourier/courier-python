from .exceptions import CourierAPIException


class Events():
    key = "events"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def list(self):
        """
        Fetch the list of events.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains results
        """

        resp = self.session.get(self.uri)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get(self, event_id):
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
        url = "%s/%s" % (self.uri, event_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def replace(self, event_id, notification_id, type="notification"):
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
