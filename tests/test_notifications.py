import responses

from trycourier.client import Courier


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

    assert r == {'paging': {'cursor': None, 'more': False}, 'results': []}


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
    r = c.notifications.get_content('my-notification')

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
    r = c.notifications.get_draft_content('my-notification')

    assert r == {'blocks': [], 'channels': []}


@responses.activate
def test_success_put_locales():
    responses.add(
        responses.PUT,
        'https://api.courier.com/notifications/my-notification/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.put_locales('my-notification', [], [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_put_draft_locales():
    responses.add(
        responses.PUT,
        'https://api.courier.com/notifications/my-notification/draft/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.put_draft_locales('my-notification', [], [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_put_locale():
    responses.add(
        responses.PUT,
        'https://api.courier.com/notifications/my-notification/locales/my-locale',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.put_locale('my-notification', 'my-locale', [], [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_put_draft_locale():
    responses.add(
        responses.PUT,
        'https://api.courier.com/notifications/my-notification/draft/locales/my-locale',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.put_draft_locale(
        'my-notification', 'my-locale', [], [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_post_block_locales():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/blocks/my-block/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.post_block_locales(
        'my-notification', 'my-block', [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_post_draft_block_locales():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/draft/blocks/my-block/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.post_draft_block_locales(
        'my-notification', 'my-block', [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_post_channel_locales():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/channels/my-channel/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.post_channel_locales(
        'my-notification', 'my-channel', [])

    assert len(responses.calls) == 1


@responses.activate
def test_success_post_draft_channel_locales():
    responses.add(
        responses.POST,
        'https://api.courier.com/notifications/my-notification/draft/channels/my-channel/locales',
        status=200,
        content_type='application/json'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.notifications.post_draft_channel_locales(
        'my-notification', 'my-channel', [])

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
    r = c.notifications.get_submission_checks(
        'my-notification', 'my-submission')

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
    r = c.notifications.put_submission_checks(
        'my-notification', 'my-submission', [])

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
    r = c.notifications.delete_submission_checks(
        'my-notification', 'my-submission')

    assert len(responses.calls) == 1
