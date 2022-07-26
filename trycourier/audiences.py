from .exceptions import CourierAPIException


class Audiences():
    key = "audiences"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def put_audience(self, audience_id, audience):
        """
        Create a new Audiences messaging job

        Args:
            message (dict): Audience Defintion - audience_id, name,
            description, filter
        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a audience definition
        """
        url = "%s/%s" % (self.uri, audience_id)
        payload = {
            'name': audience.get('name'),
            'description': audience.get('description'),
            'filter': audience.get('filter')
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_audience(self, audience_id):
        """
        Gets Audience by id

        Args:
            audience_id: A audience id to get the details of

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains audience definition
        """
        url = "%s/%s" % (self.uri, audience_id)
        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_audience_members(self, audience_id, cursor=None):
        """
        Gets Audience members by id

        Args:
            audience_id: An audience id to get the members of
            cursor: optional pointer to for fetching subsequent result pages

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains user details and paging info
        """

        params = {}

        if cursor:
            params['cursor'] = cursor

        url = "%s/%s/members" % (self.uri, audience_id)
        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_audiences(self, cursor=None):
        """
        Gets all Audiences associated with the `authorization_token`

        Args:
            cursor: optional pointer to for fetching subsequent result pages

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains user details and paging info
        """

        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
