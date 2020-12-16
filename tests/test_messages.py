import responses
import pytest

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_messages_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.messages.list()

    assert r == {'paging': {}, 'items': []}


@responses.activate
def test_success_messages_list_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages?cursor=12&event=34&recipient=56'
        '&notification=78&messageId=91&list=23',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.messages.list(cursor='12', event='34', recipient='56',
                        notification='78', message_id='91', list_id='23')

    assert r == {'paging': {}, 'items': []}


@responses.activate
def test_fail_messages_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.messages.list()


@responses.activate
def test_success_messages_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages/my.message.id',
        status=200,
        content_type='application/json',
        body='{"id": "my.message.id", "name": "My Message"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.messages.get("my.message.id")

    assert r == {"id": "my.message.id", "name": "My Message"}


@responses.activate
def test_fail_messages_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages/my.message.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.messages.get("my.message.id")


@responses.activate
def test_success_messages_get_history():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages/my.message.id/history',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.messages.get_history(message_id="my.message.id")

    assert r == {'results':[]}

@responses.activate
def test_success_messages_get_history_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages/my.message.id/history?type=my.type',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.messages.get_history(message_id="my.message.id", type="my.type")

    assert r == {'results':[]}


@responses.activate
def test_fail_messages_get_history():
    responses.add(
        responses.GET,
        'https://api.courier.com/messages/my.message.id/history',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.messages.get_history("my.message.id")





