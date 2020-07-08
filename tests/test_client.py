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
        brand='W50NC77P524K14M5300PGPEK4JMJ',
        preferences={'preferrred_channel': 'email'},
        override={'provider': {}}
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"status": "ok"}
    assert request_params["profile"] == {'email': 'test@example.com'}
    assert request_params["brand"] == 'W50NC77P524K14M5300PGPEK4JMJ'
    assert request_params["preferences"] == {'preferrred_channel': 'email'}
    assert request_params["override"] == {'provider': {}}


@responses.activate
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


@responses.activate
def test_success_get_profile():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/profiles/1234',
        status=200,
        content_type='application/json',
        body='{"profile": { "email": "test@example.com"}}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_profile("1234")

    assert r == {"profile": {"email": "test@example.com"}}


@responses.activate
def test_fail_get_profile():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/profiles/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_profile("1234")


@responses.activate
def test_success_replace_profile():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/profiles/1234',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')
    r = c.replace_profile("1234", profile)

    assert r == {"status": "SUCCESS"}


@responses.activate
def test_fail_replace_profile():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/profiles/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.replace_profile("1234", profile)


@responses.activate
def test_success_merge_profile():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/profiles/1234',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')
    r = c.merge_profile("1234", profile)

    assert r == {"status": "SUCCESS"}


@responses.activate
def test_fail_merge_profile():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/profiles/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.merge_profile("1234", profile)


@responses.activate
def test_success_get_messages():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/messages',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_messages()

    assert r == {"paging": {}, "results": []}


@responses.activate
def test_success_get_messages_with_params():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/messages?cursor=ABCD1234&recipient=1234',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_messages(cursor="ABCD1234", recipient="1234")

    assert r == {"paging": {}, "results": []}


@responses.activate
def test_fail_get_messages():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/messages',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_messages()


@responses.activate
def test_success_get_message():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/messages/1234',
        status=200,
        content_type='application/json',
        body='{"status": "DELIVERED"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_message(
        message_id='1234',
    )

    assert r == {"status": "DELIVERED"}


@responses.activate
def test_fail_get_message():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/messages/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_message(
            message_id='1234',
        )


@responses.activate
def test_success_get_events():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/events',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_events()

    assert r == {"results": []}


@responses.activate
def test_fail_get_events():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/events',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_events()


@responses.activate
def test_success_get_event():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/events/1234',
        status=200,
        content_type='application/json',
        body='{"status": "DELIVERED"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_event(
        event_id='1234',
    )

    assert r == {"status": "DELIVERED"}


@responses.activate
def test_fail_get_event():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/events/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_event(
            event_id='1234',
        )


@responses.activate
def test_success_replace_event():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/events/1234',
        status=200,
        content_type='application/json',
        body='{"id": "notification-id-1", "type": "notification"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.replace_event("1234", notification_id="notification-id-1")

    assert r == {"id": "notification-id-1", "type": "notification"}


@responses.activate
def test_fail_replace_event():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/events/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.replace_event("1234", notification_id="notification-id-1")


@responses.activate
def test_success_get_brands():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/brands',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_brands()

    assert r == {"paging": {}, "results": []}


@responses.activate
def test_success_get_brands_with_params():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/brands?cursor=ABCD1234',
        status=200,
        content_type='application/json',
        body='{"paging": {}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_brands(cursor="ABCD1234")

    assert r == {"paging": {}, "results": []}


@responses.activate
def test_fail_get_brands():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/brands',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_brands()


@responses.activate
def test_success_get_brand():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/brands/1234',
        status=200,
        content_type='application/json',
        body='{"status": "DELIVERED"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.get_brand(brand_id='1234')

    assert r == {"status": "DELIVERED"}


@responses.activate
def test_fail_get_brand():
    responses.add(
        responses.GET,
        'https://api.trycourier.app/brands/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.get_brand(brand_id='1234')


@responses.activate
def test_success_create_brand():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/brands',
        status=200,
        content_type='application/json',
        body='{"id": "1234", "name": "my brand"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.create_brand(name="my brand", settings={})

    assert r == {"id": "1234", "name": "my brand"}


@responses.activate
def test_success_create_brand_with_options():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/brands',
        status=200,
        content_type='application/json',
        body='{"id": "1234", "name": "my brand"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.create_brand(name="my brand",
                       settings={},
                       id='1234',
                       snippets={
                           'format': 'handlebars',
                           'name': 'test',
                           'value': '{{test}}'
                       })

    assert r == {"id": "1234", "name": "my brand"}


@responses.activate
def test_fail_create_brand():
    responses.add(
        responses.POST,
        'https://api.trycourier.app/brands',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.create_brand(name="my brand", settings={})


@responses.activate
def test_success_replace_brand():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/brands/1234',
        status=200,
        content_type='application/json',
        body='{"id": "1234", "name": "my brand"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.replace_brand("1234", name="my brand", settings={})

    assert r == {"id": "1234", "name": "my brand"}


@responses.activate
def test_success_replace_brand_with_options():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/brands/1234',
        status=200,
        content_type='application/json',
        body='{"id": "1234", "name": "my brand"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.replace_brand("1234",
                        name="my brand",
                        settings={},
                        snippets={
                           'format': 'handlebars',
                           'name': 'test',
                           'value': '{{test}}'
                        })

    assert r == {"id": "1234", "name": "my brand"}


@responses.activate
def test_fail_replace_brand():
    responses.add(
        responses.PUT,
        'https://api.trycourier.app/brands/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.replace_brand("1234",
                        name="my brand",
                        settings={})


@responses.activate
def test_success_delete_brand():
    responses.add(
        responses.DELETE,
        'https://api.trycourier.app/brands/1234',
        status=204
    )

    c = Courier(auth_token='123456789ABCDF')
    c.delete_brand('1234')

    assert len(responses.calls) == 1


@responses.activate
def test_fail_delete_brand():
    responses.add(
        responses.DELETE,
        'https://api.trycourier.app/brands/1234',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.delete_brand('1234')
