from .exceptions import CourierAPIException


class Accounts():
    key = "accounts"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def get_account(self, account_id):
        """
        Gets an account

        Args:
            account_id: An account to get the details of

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains account object
        """
        url = "%s/%s" % (self.uri, account_id)
        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_accounts(self, limit=None, starting_after=None):
        """
        Lists accounts

        Args:
            limit: The number of accounts to return (default 20, max 100)
            starting_after: Value of next_page from previous response

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains accounts items and paging info
        """

        params = {}

        if limit:
            params['limit'] = limit

        if starting_after:
            params['starting_after'] = starting_after

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_account(self, account_id, account):
        """
        Create a new account

        Args:
            account (dict): Account Defintion - name, parent_account_id,
            default_preferences, properties, user_profile, brand_id
        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains an account definition
        """
        url = "%s/%s" % (self.uri, account_id)
        payload = {
            'name': account.get('name'),
            'parent_account_id': account.get('parent_account_id'),
            'default_preferences': account.get('default_preferences'),
            'properties': account.get('properties'),
            'user_profile': account.get('user_profile'),
            'brand_id': account.get('brand_id')
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def delete_account(self, account_id):
        """
        Delete an account

        Args:
            account_id (str): Account you want to delete

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s" % (self.uri, account_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)
