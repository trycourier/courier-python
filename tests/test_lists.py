import json
import responses
import pytest

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException


@responses.activate
def test_success_lists_send_with_list():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.send(
        event='1234',
        list='my.list.id'
    )

    assert r == {"status": "ok"}


@responses.activate
def test_success_lists_send_with_pattern():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.send(
        event='1234',
        pattern='my.list.*'
    )

    assert r == {"status": "ok"}


@responses.activate
def test_success_lists_send_with_options():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.send(
        event='1234',
        list='my.list.id',
        brand='W50NC77P524K14M5300PGPEK4JMJ',
        override={'provider': {}}
    )

    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"status": "ok"}
    assert request_params["brand"] == 'W50NC77P524K14M5300PGPEK4JMJ'
    assert request_params["override"] == {'provider': {}}


@responses.activate
def test_success_lists_send_idempotent():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.send(
        event='1234',
        list='my.list.id',
        idempotency_key='1234ABCD'
    )

    assert responses.calls[0].request.headers.get(
        'Idempotency-Key') == '1234ABCD'
    assert r == {"status": "ok"}


@responses.activate
def test_fail_lists_send():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.send(
            event='1234',
            list='my.list.id'
        )


@responses.activate
def test_fail_lists_send_with_list_and_pattern():
    responses.add(
        responses.POST,
        'https://api.courier.com/send/list',
        status=200,
        content_type='application/json',
        body='{"status": "ok"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(Exception):
        c.lists.send(
            event='1234',
            list='my.list.id',
            pattern='my.list.*'
        )


@responses.activate
def test_success_lists_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.list()

    assert r == {'paging': {}, 'items': []}


@responses.activate
def test_success_lists_list_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists?cursor=1234&pattern=my.list.*',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.list(cursor='1234', pattern='my.list.*')

    assert r == {'paging': {}, 'items': []}


@responses.activate
def test_fail_lists_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.list()


@responses.activate
def test_success_lists_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists/my.list.id',
        status=200,
        content_type='application/json',
        body='{"id": "my.list.id", "name": "My List"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.get("my.list.id")

    assert r == {"id": "my.list.id", "name": "My List"}


@responses.activate
def test_fail_lists_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists/my.list.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.get("my.list.id")


@responses.activate
def test_success_lists_put():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.put("my.list.id", "My List")

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_put():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id',
        status=400,
        content_type='application/json',
        body='{"message": "Error Message"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.put("my.list.id", "My List")


@responses.activate
def test_success_lists_delete():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/lists/my.list.id',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.delete("my.list.id")

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_delete():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/lists/my.list.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.delete("my.list.id")


@responses.activate
def test_success_lists_restore():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/restore',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.restore("my.list.id")

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_restore():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/restore',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.restore("my.list.id")


@responses.activate
def test_success_lists_get_subscriptions():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists/my.list.id/subscriptions',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.get_subscriptions("my.list.id")

    assert r == {"paging": {}, "items": []}


@responses.activate
def test_success_lists_get_subscriptions_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists/my.list.id/subscriptions?cursor=1234',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "items": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.get_subscriptions("my.list.id", cursor="1234")

    assert r == {"paging": {}, "items": []}


@responses.activate
def test_fail_lists_get_subscriptions():
    responses.add(
        responses.GET,
        'https://api.courier.com/lists/my.list.id/subscriptions',
        status=404,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.get_subscriptions("my.list.id")


@responses.activate
def test_success_lists_put_subscriptions():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/subscriptions',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.put_subscriptions("my.list.id", ["1234", "4321"])

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_put_subscriptions():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/subscriptions',
        status=400,
        content_type='application/json',
        body='{"message": "Error Message"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.put_subscriptions("my.list.id", ["1234", "4321"])


@responses.activate
def test_success_lists_subscribe():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/subscriptions/1234',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.subscribe("my.list.id", "1234")

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_subscribe():
    responses.add(
        responses.PUT,
        'https://api.courier.com/lists/my.list.id/subscriptions/1234',
        status=400,
        content_type='application/json',
        body='{"message": "Error Message"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.subscribe("my.list.id", "1234")


@responses.activate
def test_success_lists_unsubscribe():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/lists/my.list.id/subscriptions/1234',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.lists.unsubscribe("my.list.id", "1234")

    assert len(responses.calls) == 1


@responses.activate
def test_fail_lists_unsubscribe():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/lists/my.list.id/subscriptions/1234',
        status=404,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.unsubscribe("my.list.id", "1234")


@responses.activate
def test_success_lists_find_by_recipient_id():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/1234/lists',
        status=200,
        content_type='application.json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.find_by_recipient_id("1234")

    assert r == {'paging': {}, 'results': []}


@responses.activate
def test_success_lists_find_by_recipient_id_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/1234/lists?cursor=1234',
        status=200,
        content_type='application.json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.lists.find_by_recipient_id("1234", cursor="1234")

    assert r == {'paging': {}, 'results': []}


@responses.activate
def test_fail_lists_find_by_recipient_id():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/1234/lists',
        status=400,
        content_type='application.json',
        body='{"message": "Error Message"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.lists.find_by_recipient_id("1234")
