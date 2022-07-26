from .exceptions import CourierAPIException


class AuditEvents():
    key = "audit-events"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def get_audit_event(self, audit_event_id):
        """
        Gets an audit event

        Args:
            audit_event_id: An audit event to get the details of

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains audit event
        """
        url = "%s/%s" % (self.uri, audit_event_id)
        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def list_audit_events(self, cursor=None):
        """
        Lists audit events

        Args:
            cursor: optional pointer to fetch subsequent result pages

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains audit event details and paging info
        """

        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
