import json
import responses
import pytest
from os import environ

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_invoke():
    responses.add(
        responses.POST,
        'https://api.courier.com/automations/invoke',
        status=200,
        content_type='application/json',
        body='{"runId": "12345"}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.automations.invoke(
        automation={'steps': [{ 'action': 'send' }]},
        brand='W50NC77P524K14M5300PGPEK4JMJ',
        data={'foo': 'bar'},
        profile={'email': 'test@example.com'},
        recipient='4321',
        template='template-001'
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"runId": "12345"}
    assert request_params["automation"] == {'steps': [{ 'action': 'send' }]}
    assert request_params["brand"] == 'W50NC77P524K14M5300PGPEK4JMJ'
    assert request_params["data"] == {'foo': 'bar'}
    assert request_params["profile"] == {'email': 'test@example.com'}
    assert request_params["recipient"] == '4321'
    assert request_params["template"] == 'template-001'

@responses.activate
def test_fail_invoke():
    responses.add(
        responses.POST,
        'https://api.courier.com/automations/invoke',
        status=500,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.automations.invoke(automation={})

@responses.activate
def test_success_invoke_template():
    responses.add(
        responses.POST,
        'https://api.courier.com/automations/my-automation-template/invoke',
        status=200,
        content_type='application/json',
        body='{"runId": "12345"}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.automations.invoke_template(
        template_id='my-automation-template',
        brand='W50NC77P524K14M5300PGPEK4JMJ',
        data={'foo': 'bar'},
        profile={'email': 'test@example.com'},
        recipient='4321',
        template='template-001'
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"runId": "12345"}
    assert request_params["brand"] == 'W50NC77P524K14M5300PGPEK4JMJ'
    assert request_params["data"] == {'foo': 'bar'}
    assert request_params["profile"] == {'email': 'test@example.com'}
    assert request_params["recipient"] == '4321'
    assert request_params["template"] == 'template-001'

@responses.activate
def test_fail_invoke_template():
    responses.add(
        responses.POST,
        'https://api.courier.com/automations/my-automation-template/invoke',
        status=500,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.automations.invoke_template(template_id='my-automation-template')
