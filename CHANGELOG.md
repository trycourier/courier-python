# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased][unreleased]

## [v1.8.0] - 2021-04-07

### Added

- Support for [Automation API](https://docs.courier.com/reference/automation-api) by @tk26
  - `POST /automations/invoke` with `client.automations.invoke_ad_hoc_automation` method
  - `POST /automations/{template_id}/invoke` with `client.automations.invoke_automation_template` method

## [v1.7.0] - 2020-12-18

### Added

- Environment Variables for Basic Authentication:
  - `COURIER_AUTH_USERNAME` and `COURIER_AUTH_PASSWORD`
- Environment Variable to set Base URL:
  - `COURIER_BASE_URL`
- Support for [Messages API](https://docs.courier.com/reference/messages-api) by @jrweingart

  - `GET /messages` with `client.messages.list` method
  - `GET /messages/{message_id}` with `client.messages.get` method
  - `GET /messages/{message_id}/history` with `client.messages.get_history` method

- Support for [Profiles API](https://docs.courier.com/reference/profiles-api) by @jrweingart
  - `GET /profiles/{recipient_id}` with `client.profiles.get` method
  - `GET /profiles/{recipient_id}/lists` with `client.profiles.get_subscriptions` method
  - `PUT /profiles/{recipient_id}` with `client.profiles.replace` and `client.profiles.add` methods
  - `PATCH /profiles/{recipient_id}` with `client.profiles.patch` method
  - `POST /profiles/{recipient_id}` with `client.profiles.merge` method

## [v1.6.0] - 2020-11-09

### Added

- Support for [Lists API](https://docs.courier.com/reference/lists-api) by @aydrian
  - `POST /send/list` with `client.lists.send` method
  - `GET /profiles/{recipient_id}/lists` with `client.lists.find_by_recipient_id` method
  - `GET /lists` with `client.lists.list` method
  - `GET /lists/{list_id}` with `client.lists.get` method
  - `PUT /lists/{list_id}` with `client.lists.put` method
  - `DELETE /lists/{list_id}` with `client.lists.delete` method
  - `PUT /lists/{list_id}/restore` with `client.lists.restore` method
  - `GET /lists/{list_id}/subscriptions` with `client.lists.get_subscriptions` method
  - `PUT /lists/{list_id}/subscriptions` with `client.lists.put_subscriptions` method
  - `PUT /lists/{list_id}/subscriptions/{recipient_id}` with `client.lists.subscribe` method
  - `DELETE /lists/{list_id}/subscriptions/{recipient_id}` with `client.lists.unsubscribe` method

### Changed

- Default `base_url` is now `api.courier.com`

## [v1.5.0] - 2020-07-27

### Added

- Support for Idempotency. You can now pass an `idempotency_key` to the following methods by @aydrian:
  - `send()`
  - `merge_profile()`
  - `create_brand()`

## [v1.4.0] - 2020-07-09

### Added

- Added the ability to configure timeouts when creating a client with a default of 5 seconds for both
  Connect and Read by @aydrian

## [v1.3.0] - 2020-07-09

### Added

- Support for [Brands API](https://docs.courier.com/reference/brands-api) by @aydrian
  - `GET /brands` with `get_brands` method
  - `GET /brands/:brand_id` with `get_brand` method
  - `POST /brands` with `create_brand` method
  - `PUT /brands/:brand_id` with `replace_brand` method
  - `DELETE /brands/:brand_id` with `delete_brand` method
- Support for specifying notification brand during [send](https://docs.courier.com/reference/send-api#sendmessage) by @aydrian

### Changed

- Updated [requests](https://pypi.org/project/requests/) library to v2.24.0

## [v1.2.0] - 2020-06-18

### Added

- Support for [`GET /messages/{message_id}`](https://docs.courier.com/reference/messages-api#getmessagebyid) with `get_message` method by @jackwestmoretab (Thank you! :tada:)
- Support for [`GET /messages`](https://docs.courier.com/reference/messages-api#getmessages) with `get_messages` method by @aydrian
- Support for [Events API](https://docs.courier.com/reference/events-api) with `get_events`, `get_event`, and `replace_event` methods by @aydrian

## [v1.1.0] - 2020-03-20

### Added

- Support for [Profiles API](https://docs.courier.com/reference/profiles-api) with `get_profile`, `replace_profile`, and `merge_profile` methods by @aydrian

## v1.0.0 - 2020-03-06

Initial release. Supports Python 3.5+. Supports Send API.

[unreleased]: https://github.com/trycourier/courier-python/compare/v1.8.0...HEAD
[v1.8.0]: https://github.com/trycourier/courier-python/compare/v1.7.0...v1.8.0
[v1.7.0]: https://github.com/trycourier/courier-python/compare/v1.6.0...v1.7.0
[v1.6.0]: https://github.com/trycourier/courier-python/compare/v1.5.0...v1.6.0
[v1.5.0]: https://github.com/trycourier/courier-python/compare/v1.4.0...v1.5.0
[v1.4.0]: https://github.com/trycourier/courier-python/compare/v1.3.0...v1.4.0
[v1.3.0]: https://github.com/trycourier/courier-python/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/trycourier/courier-python/compare/v1.1.0...v1.2.0
[v1.1.0]: https://github.com/trycourier/courier-python/compare/v1.0.0...v1.1.0
