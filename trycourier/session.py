from base64 import b64encode
from requests import Session


class CourierAPISession(Session):

    def __init__(self, *args, **kwargs):
        """
        Creates a new CoreAPISession instance.
        """
        super(CourierAPISession, self).__init__(*args, **kwargs)

        self.headers.update({
            'Content-Type': 'application/json'
        })

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
