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
        url = "%s/%s" % (self.uri, list_id)

        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put(self, list_id, name):
        url = "%s/%s" % (self.uri, list_id)
        payload = {
            'name': name
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def delete(self, list_id):
        url = "%s/%s" % (self.uri, list_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def restore(self, list_id):
        url = "%s/%s/restore" % (self.uri, list_id)

        resp = self.session.put(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def get_subscriptions(self, list_id, cursor=None):
        url = "%s/%s/subscriptions" % (self.uri, list_id)
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def put_subscriptions(self, list_id, recipients):
        url = "%s/%s/subscriptions" % (self.uri, list_id)
        payload = {
            'recipients': recipients
        }

        resp = self.session.put(url, json=payload)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def subscribe(self, list_id, recipient_id):
        url = "%s/%s/subscriptions/%s" % (self.uri, list_id, recipient_id)

        resp = self.session.put(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def unsubscribe(self, list_id, recipient_id):
        url = "%s/%s/subscriptions/%s" % (self.uri, list_id, recipient_id)

        resp = self.session.delete(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

    def find_by_recipient_id(self, recipient_id, cursor=None):
        url = "%s/profiles/%s/lists" % (self.base_url, recipient_id)
        params = {}

        if cursor:
            params['cursor'] = cursor

        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
