import json
import responses
import pytest
from os import environ
from datetime import datetime, timedelta

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_create_job():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk',
        status=200,
        content_type='application/json',
        body='{"jobId": "12345"}'
    )
    c = Courier(auth_token='123456789ABCDF')
    expiration_date = (datetime.now()+timedelta(days=7)).isoformat()
    r = c.bulk.create_job(
        message={'event': 'foo'},
        idempotency_key='1234ABCD',
        idempotency_expiration=expiration_date
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"jobId": "12345"}
    assert responses.calls[0].request.headers.get(
        'Idempotency-Key') == '1234ABCD'
    assert responses.calls[0].request.headers.get(
        'x-idempotency-expiration') == expiration_date
    assert request_params["message"] == {'event': 'foo'}

@responses.activate
def test_fail_create_job():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk',
        status=500,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.bulk.create_job(message={})

@responses.activate
def test_success_ingest_users():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk/12345',
        status=200,
        content_type='application/json',
        body='{"errors": [], "total": 1}'
    )
    c = Courier(auth_token='123456789ABCDF')
    expiration_date = (datetime.now()+timedelta(days=7)).isoformat()
    r = c.bulk.ingest_users(
        job_id='12345',
        users=[{ 'profile': { 'email': 'foo@bar.com' } }],
        idempotency_key='1234ABCD',
        idempotency_expiration=expiration_date
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert r == {"errors": [], "total" : 1}
    assert responses.calls[0].request.headers.get(
        'Idempotency-Key') == '1234ABCD'
    assert responses.calls[0].request.headers.get(
        'x-idempotency-expiration') == expiration_date
    assert request_params["users"] == [{'profile': {'email': 'foo@bar.com'}}]

@responses.activate
def test_fail_ingest_users():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk/12345',
        status=500,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.bulk.ingest_users(
        job_id='12345',
        users=[{ 'profile': { 'email': 'foo@bar.com' } }]
    )

@responses.activate
def test_success_run_job():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk/12345/run',
        status=202,
        content_type='application/json',
        body='{}'
    )
    c = Courier(auth_token='123456789ABCDF')
    expiration_date = (datetime.now()+timedelta(days=7)).isoformat()
    r = c.bulk.run_job(
        job_id='12345',
        idempotency_key='1234ABCD',
        idempotency_expiration=expiration_date
    )
    request_params = json.loads(
        responses.calls[0].request.body.decode('utf-8'))

    assert responses.calls[0].request.headers.get(
        'Idempotency-Key') == '1234ABCD'
    assert responses.calls[0].request.headers.get(
        'x-idempotency-expiration') == expiration_date

@responses.activate
def test_fail_run_job():
    responses.add(
        responses.POST,
        'https://api.courier.com/bulk/12345/run',
        status=500,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.bulk.run_job(job_id='12345')

@responses.activate
def test_success_get_job():
    responses.add(
        responses.GET,
        'https://api.courier.com/bulk/job.id',
        status=200,
        content_type='application/json',
        body='{"job": {"definition": {"event": "RR4NDQ7NZ24A8TKPWVBEDGE15E9A"},"enqueued": 1,"failures": 0,"received": 1,"status": "COMPLETED"}}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.bulk.get_job("job.id")

    assert r == {
        "job": {
            "definition": {
                "event": "RR4NDQ7NZ24A8TKPWVBEDGE15E9A"
            },
    		"enqueued": 1,
            "failures": 0,
            "received": 1,
            "status": "COMPLETED"
	    }
    }

@responses.activate
def test_fail_get_job():
    responses.add(
        responses.GET,
        'https://api.courier.com/bulk/job.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.bulk.get_job("job.id")

@responses.activate
def test_success_get_job_users():
    responses.add(
        responses.GET,
        'https://api.courier.com/bulk/job.id/users?cursor=abc',
        status=200,
        content_type='application/json',
        body='{"paging": {"cursor": "def" }, "items": [{ "profile": {"email": "foo@bar.com"},  "recipient": "NEfgqX8CLFZ8uTBWq9zdH", "messageId": "1-61eb0bd1-9ecd21e534ba85c099211b63", "status": "ENQUEUED" }]}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.bulk.get_job_users("job.id", cursor='abc')

    assert r == {
        "items": [
            {
                "profile": {
                    "email": "foo@bar.com"
                },
                "recipient": "NEfgqX8CLFZ8uTBWq9zdH",
                "messageId": "1-61eb0bd1-9ecd21e534ba85c099211b63",
                "status": "ENQUEUED"
            }
        ],
        "paging": {
            "cursor": "def"
        }
    }

@responses.activate
def test_fail_get_job_users():
    responses.add(
        responses.GET,
        'https://api.courier.com/bulk/job.id/users?cursor=abc',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.bulk.get_job_users("job.id", cursor='abc')
