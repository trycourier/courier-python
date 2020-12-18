import responses
import pytest

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_profiles_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"profile":{}}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.get("profile.id")

    assert r == {'profile':{}}


@responses.activate
def test_fail_profiles_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/profile.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.profiles.get('profile.id')


@responses.activate
def test_success_profiles_get_subscriptions():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/profile.id/lists',
        status=200,
        content_type='application/json',
        body='{"paging":{}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.get_subscriptions('profile.id')

    assert r == {'paging':{}, 'results':[]}


@responses.activate
def test_success_profiles_get_subscriptions_with_params():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/profile.id/lists?cursor=456',
        status=200,
        content_type='application/json',
        body='{"paging":{}, "results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.get_subscriptions(recipient_id='profile.id', cursor="456")

    assert r == {'paging':{}, 'results':[]}


@responses.activate
def test_fail_profiles_get_subscriptions():
    responses.add(
        responses.GET,
        'https://api.courier.com/profiles/profile.id/lists',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.profiles.get_subscriptions("profile.id")

@responses.activate
def test_success_profiles_add():
    responses.add(
        responses.PUT,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )
    profile = {
        "email": "jane@doe.com"
    }
    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.add("profile.id", profile)

    assert r == {"status": "SUCCESS"}

@responses.activate
def test_success_profiles_replace():
    responses.add(
        responses.PUT,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )
    profile={
        "email":"jane@doe.com"
    }
    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.replace("profile.id", profile)

    assert r == {"status":"SUCCESS"}


@responses.activate
def test_fail_profiles_replace():
    responses.add(
        responses.PUT,
        'https://api.courier.com/profiles/profile.id',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    profile = {
        "email": "jane@doei.com"
    }

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.profiles.replace("profile.id", profile)


@responses.activate
def test_success_profiles_merge():
    responses.add(
        responses.POST,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )

    profile = {
        "email": "jane@doe.com"
    }

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.merge("profile.id", profile)

    assert r == {"status": "SUCCESS"}


@responses.activate
def test_success_profiles_merge_idempotent():
    responses.add(
        responses.POST,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.merge("profile.id", profile, idempotency_key="1234ABCD")

    assert responses.calls[0].request.headers.get(
        'Idempotency-Key') == '1234ABCD'
    assert r == {"status": "SUCCESS"}


@responses.activate
def test_fail_profiles_merge():
    responses.add(
        responses.POST,
        'https://api.courier.com/profiles/profile.id',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.profiles.merge("profile.id", profile)

@responses.activate
def test_success_profiles_patch():
    responses.add(
        responses.PATCH,
        'https://api.courier.com/profiles/profile.id',
        status=200,
        content_type='application/json',
        body='{"status": "SUCCESS"}'
    )

    operations=[
        {
            "op":"add",
            "path": "/number",
            "value": 4
        },
        {
            "op":"replace",
            "path": "/number",
            "value": 5
        },
        {
            "op":"copy",
            "from":"/number",
            "path":"/test_num"
        }
    ]

    c = Courier(auth_token='123456789ABCDF')
    r = c.profiles.patch("profile.id", operations)

    assert r == {"status": "SUCCESS"}

@responses.activate
def test_fail_profiles_patch():
    responses.add(
        responses.PATCH,
        'https://api.courier.com/profiles/profile.id',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    profile = {
        "email": "text@example.com"
    }

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.profiles.patch("profile.id", profile)