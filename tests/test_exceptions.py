import json
from requests import Response

from trycourier.exceptions import CourierAPIException


def _response(content):
    r = Response()
    r.status_code = 400
    r.url = 'http://someurl'
    r._content = json.dumps(content).encode()
    return r


def test_CourierAPIException():
    r = _response({'message': 'An error occured'})
    e = CourierAPIException(r)

    assert e.message == 'Call to http://someurl returned 400\nAn error occured'
    assert e.response == r
