from base64 import b64encode
from requests import Session
from requests.adapters import HTTPAdapter


class MyHTTPAdapter(HTTPAdapter):

    def __init__(self, timeout=None, *args, **kwargs):
        self.timeout = timeout
        super(MyHTTPAdapter, self).__init__(*args, **kwargs)

    def send(self, *args, **kwargs):
        kwargs['timeout'] = self.timeout
        return super(MyHTTPAdapter, self).send(*args, **kwargs)


class CourierAPISession(Session):

    def __init__(self, timeout=5, *args, **kwargs):
        """
        Creates a new CoreAPISession instance.
        """
        super(CourierAPISession, self).__init__(*args, **kwargs)

        self.headers.update({
            'Content-Type': 'application/json'
        })

        self.mount("https://", MyHTTPAdapter(timeout=timeout))

    def init_library_version(self, version):
        self.headers.update({
            'User-Agent': 'courier-python/{}'.format(version)
        })

    def init_token_auth(self, auth_token):
        self.headers.update({
            'Authorization': 'Bearer {}'.format(auth_token)
        })

    def init_basic_auth(self, username, password):
        credentials = b64encode('{}:{}'.format(username, password).encode())
        self.headers.update({
            'Authorization': 'Basic {}'.format(credentials.decode())
        })


__all__ = ['CourierAPISession']
