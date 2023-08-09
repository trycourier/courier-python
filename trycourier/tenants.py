from .exceptions import CourierAPIException


class Tenants():
    key = "tenants"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def get_tenant(self, tenant_id):
        """
        Gets a tenant

        Args:
            tenant_id: A tenant to get the details of

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains tenant object
        """
        url = "%s/%s" % (self.uri, tenant_id)
        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_tenants(self, limit=None, cursor=None):
        """
        Lists tenants

        Args:
            limit: The number of tenants to return (default 20, max 100)
            cursor: Value of next_page from previous response

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains tenants items and paging info
        """

        params = {}

        if limit:
            params['limit'] = limit

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(self.uri, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_tenant(self, tenant_id, tenant):
        """
        Create a new tenant

        Args:
            tenant (dict): tenant Defintion - name, parent_tenant_id,
            default_preferences, properties, user_profile, brand_id
        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a tenant definition
        """
        url = "%s/%s" % (self.uri, tenant_id)
        payload = {
            'name': tenant.get('name'),
            'parent_tenant_id': tenant.get('parent_tenant_id'),
            'default_preferences': tenant.get('default_preferences'),
            'properties': tenant.get('properties'),
            'user_profile': tenant.get('user_profile'),
            'brand_id': tenant.get('brand_id')
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def delete_tenant(self, tenant_id):
        """
        Delete a tenant

        Args:
            tenant_id (str): tenant you want to delete

        Raises:
            CourierAPIException: Any error returned by the Courier API
        """
        url = "%s/%s" % (self.uri, tenant_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)
