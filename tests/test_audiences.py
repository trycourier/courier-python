import json
import responses
import pytest
from os import environ
from datetime import datetime, timedelta

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException


@responses.activate
def test_success_put_audience():
    responses.add(
        responses.PUT,
        'https://api.courier.com/audiences/software-engineers-from-sf',
        status=200,
        content_type='application/json',
        body='{"audience": {"id": "software-engineers-from-sf", "name": "", "description": "", "created_at": "2022-03-24T18:56:49.181Z", "updated_at": "2022-03-24T19:54:37.982Z", "filter": {"path": "title", "value": "Software Engineer", "operator": "EQ"}}}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.audiences.put_audience(
        'software-engineers-from-sf',
        audience={
            'name': '',
            'description': '',
            'filter': {
                'path': 'title',
                'value': 'Software Engineer',
                'operator': 'EQ'
            }
        },
    )

    assert r == {
        "audience": {
            "id": "software-engineers-from-sf",
            "name": "",
            "description": "",
            "created_at": "2022-03-24T18:56:49.181Z",
            "updated_at": "2022-03-24T19:54:37.982Z",
            "filter": {
                "path": "title",
                "value": "Software Engineer",
                "operator": "EQ"
            }
        }
    }


@responses.activate
def test_fail_put_audience():
    responses.add(
        responses.PUT,
        'https://api.courier.com/audiences/software-engineers-from-sf',
        status=400,
        content_type='application/json',
        body='{ "message": "filteroperator should be equal to one of the allowed values AND, EQ, GT, GTE, INCLUDES, LT, LTE, NEQ, OMIT, OR", "type": "invalid_request_error"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.audiences.put_audience(
            'software-engineers-from-sf',
            audience={
                'name': '',
                'description': '',
                'filter': {
                        'path': 'title',
                        'value': 'Software Engineer',
                        'operator': 'INVALID_FILTER_OPERATOR'
                }
            },
        )


@responses.activate
def test_success_get_audience():
    responses.add(
        responses.GET,
        'https://api.courier.com/audiences/software-engineers-from-sf',
        status=200,
        content_type='application/json',
        body='{"created_at":"2022-03-24T18:56:49.181Z","description":"Updated descriptionss","id":"software-engineers-from-sf","name":"Software Engineers From SF","filter":{"path":"title","value":"Software Engineer","operator":"EQ"},"updated_at":"2022-03-24T18:56:49.181Z"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.audiences.get_audience('software-engineers-from-sf')

    assert r == {
        "created_at": "2022-03-24T18:56:49.181Z",
        "description": "Updated descriptionss",
        "id": "software-engineers-from-sf",
        "name": "Software Engineers From SF",
        "filter": {
            "path": "title",
            "value": "Software Engineer",
            "operator": "EQ"
        },
        "updated_at": "2022-03-24T18:56:49.181Z"
    }


@responses.activate
def test_success_get_audience_members():
    responses.add(
        responses.GET,
        'https://api.courier.com/audiences/software-engineers-from-sf/members?cursor=abc',
        status=200,
        content_type='application/json',
        body='{"paging": {"cursor": "def" }, "items": [{"added_at":"2022-03-24T05:31:24.291Z","audience_id":"software-engineers-from-sf","audience_version":8,"member_id":"user_id_1","reason":"EQ(\'title\', \'Software Engineer\') => true"}]}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.audiences.get_audience_members(
        "software-engineers-from-sf", cursor='abc')

    assert r == {
        "items": [
            {
                "added_at": "2022-03-24T05:31:24.291Z",
                "audience_id": "software-engineers-from-sf",
                "audience_version": 8,
                "member_id": "user_id_1",
                "reason": "EQ('title', 'Software Engineer') => true"
            }
        ],
        "paging": {
            "cursor": "def"
        }
    }


@responses.activate
def test_success_get_audiences():
    responses.add(
        responses.GET,
        'https://api.courier.com/audiences?cursor=abc',
        status=200,
        content_type='application/json',
        body='{"paging": {"cursor": "def" }, "items": [{"created_at":"2022-03-24T18:56:49.181Z","description":"","id":"software-engineers-from-sf","name":"","filter":{"path":"title","value":"Software Engineer","operator":"EQ"},"updated_at":"2022-03-24T19:54:37.982Z"}]}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.audiences.get_audiences(cursor='abc')

    assert r == {
        "items": [
            {
                "created_at": "2022-03-24T18:56:49.181Z",
                "description": "",
                "id": "software-engineers-from-sf",
                "name": "",
                "filter": {
                    "path": "title",
                    "value": "Software Engineer",
                    "operator": "EQ"
                },
                "updated_at": "2022-03-24T19:54:37.982Z"
            }
        ],
        "paging": {
            "cursor": "def"
        }
    }
