import pytest
from requests import Request

from trycourier.session import CourierAPISession


@pytest.fixture
def _request():
    return Request('GET', 'http://someurl')


def test_request_headers(_request):
    s = CourierAPISession()
    s.init_library_version('1.0.0')
    r = s.prepare_request(_request)

    assert r.headers['Content-Type'] == 'application/json'
    assert r.headers['User-Agent'] == 'courier-python/1.0.0'


def test_token_auth(_request):
    s = CourierAPISession()
    s.init_token_auth('123456789ABCDF')
    r = s.prepare_request(_request)

    assert r.headers['Authorization'] == 'Bearer 123456789ABCDF'


def test_basic_auth(_request):
    s = CourierAPISession()
    s.init_basic_auth('user', 'pass')
    r = s.prepare_request(_request)

    assert r.headers['Authorization'] == 'Basic dXNlcjpwYXNz'
