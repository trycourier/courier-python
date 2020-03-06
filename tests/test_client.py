import json
import responses
import pytest

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException


def test_init_base_url():
    c = Courier(auth_token='123456789ABCDF',
                base_url='http://someurl')

    assert c.base_url == 'http://someurl'


def test_init_token_auth():
    c = Courier(auth_token='123456789ABCDF')

    assert 'Authorization' in c.session.headers


def test_init_basic_auth():
    c = Courier(username='user', password='pass')

    assert 'Authorization' in c.session.headers


@responses.activate
def test_success_send():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/send',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.send(
        event='1234',
        recipient='4321'
    )

    assert r == {"status": "ok"}


@responses.activate
def test_success_send_with_options():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/send',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.send(
        event='1234',
        recipient='4321',
        profile={'email': 'test@example.com'},
        preferences={'preferrred_channel': 'email'},
        override={'provider': {}}
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"status": "ok"}
    assert request_params["profile"] == {'email': 'test@example.com'}
    assert request_params["preferences"] == {'preferrred_channel': 'email'}
    assert request_params["override"] == {'provider': {}}


def test_fail_send():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/send',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.send(
            event='1234',
            recipient='4321'
        )
