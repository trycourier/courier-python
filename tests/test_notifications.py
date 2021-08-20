import json
import responses
import pytest
from os import environ

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/notifications',
        status=200,
        content_type='application/json',
        body='{"paging": {"cursor":null,"more":false}, "results": []}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.list()

    assert r == {'paging': { 'cursor': None, 'more': False }, 'results': []}

@responses.activate
def test_success_get_content():
    responses.add(
        responses.GET,
        'https://api.courier.com/notifications/my-notification/content',
        status=200,
        content_type='application/json',
        body='{"blocks": [], "channels": []}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.getContent('my-notification')

    assert r == {'blocks': [], 'channels': []}

@responses.activate
def test_success_get_draft_content():
    responses.add(
        responses.GET,
        'https://api.courier.com/notifications/my-notification/draft/content',
        status=200,
        content_type='application/json',
        body='{"blocks": [], "channels": []}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.getDraftContent('my-notification')

    assert r == {'blocks': [], 'channels': []}

@responses.activate
def test_success_post_variations():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/variations',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.postVariations('my-notification', [], [])

    assert len(responses.calls) == 1

@responses.activate
def test_success_post_draft_variations():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/draft/variations',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.postDraftVariations('my-notification', [], [])

    assert len(responses.calls) == 1

@responses.activate
def test_success_get_submission_checks():
    responses.add(
        responses.GET,
        'https://api.courier.com/notifications/my-notification/my-submission/checks',
        status=200,
        content_type='application/json',
        body='{"checks": []}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.getSubmissionChecks('my-notification', 'my-submission')

    assert r == {'checks': []}

@responses.activate
def test_success_put_submission_checks():
    responses.add(
        responses.PUT,
        'https://api.courier.com/notifications/my-notification/my-submission/checks',
        status=200,
        content_type='application/json',
        body='{"checks": []}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.putSubmissionChecks('my-notification', 'my-submission', [])

    assert r == {'checks': []}

@responses.activate
def test_success_delete_submission_checks():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/notifications/my-notification/my-submission/checks',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.deleteSubmissionChecks('my-notification', 'my-submission')

    assert len(responses.calls) == 1
