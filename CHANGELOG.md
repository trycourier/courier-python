# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased][unreleased]

## [v6.0.0] - 2024-01-26

We now use :herb: [Fern](https://buildwithfern.com/) to generate our Python 
Client. WHile this releasing has breaking changes, it comes with several 
quality of life upgrades: 
- **Endpoint coverage**: All endpoints that are supported in our Node SDK are 
  now also supported in python. 
- **Resource-scoped SDK methods**: Endpoints are scoped under their resource. For 
  example, instead of `courier.deleteBrands` the SDK now reads `courier.brands.delete(...)`  
- **Docs on Hover**: All endpoint and parameter level documentation that you see 
  on our docs website are now embedded directly within the SDKs.
- **MyPy**: All requests, responses and methods are annotated with mypy types. 
  You should get autocomplete as you use the SDK. Note that request and response models 
  are all Pydantic. 
- **Async Client**: The SDK now exports an async python client in addition to a sync
  client. Just use `AsyncCourier` : 

  ```python 
  from courier.client import AsyncCourier

  client = AsyncCourier(authorization_token="..") # defaults to os.getenv("COURIER_AUTH_TOKEN")
  ```
- **Courier Module**: The SDK exports a `courier` module and all the types are nested
  within this module. 
  ```python
  import courier

  courier. # see all the types you have access to
  ```
- **HTTPX**: The Python SDK now uses httpx instead of requests for the underlying client. 
  For advanced usecases such as proxies and transports, you can directly pass in your
  own httpx client!

## [v5.0.0] - 2023-08-09

Accounts -> Tenants

## [v4.7.0] - 2023-07-31

Add pagination attributes for accounts API

## [v4.6.0] - 2023-07-24

Adds support for Accounts API

## [v4.5.0] - 2022-07-26

Adds support for Cancel Message API

## [v4.4.0] - 2022-07-26

Adds support for Audit Events API

## [v4.3.0] - 2022-03-24

Adds support for Audiences

## [v4.2.0] - 2022-01-31

Adds support for enhanced features in Send API

## [v4.1.0] - 2022-01-25

Adds support for bulk processing API

## [v4.0.0] - 2021-11-17

Make Notifications API endpoints semantically correct

### Changed

- Notifications API
  - `client.notifications.put_block_locales` to `client.notifications.post_block_locales`
  - `client.notifications.put_draft_block_locales` to `client.notifications.post_draft_block_locales`
  - `client.notifications.put_channel_locales` to `client.notifications.post_channel_locales`
  - `client.notifications.put_draft_channel_locales` to `client.notifications.post_draft_channel_locales`

## [v3.0.0] - 2021-10-07

Adds support for notification locales

### Added:

- Notifications API
  - `PUT /notifications/{notification_id}/locales` with `client.notifications.put_locales` method
  - `PUT /notifications/{notification_id}/draft/locales` with `client.notifications.put_draft_locales` method
  - `PUT /notifications/{notification_id}/locales/{locale_id}` with `client.notifications.put_locale` method
  - `PUT /notifications/{notification_id}/draft/locales/{locale_id}` with `client.notifications.put_draft_locale` method
  - `PUT /notifications/{notification_id}/blocks/{block_id}/locales` with `client.notifications.put_block_locales` method
  - `PUT /notifications/{notification_id}/draft/blocks/{block_id}/locales` with `client.notifications.put_draft_block_locales` method
  - `PUT /notifications/{notification_id}/channels/{channel_id}/locales` with `client.notifications.put_channel_locales` method
  - `PUT /notifications/{notification_id}/draft/channels/{channel_id}/locales` with `client.notifications.put_draft_channel_locales` method

### Changed

- Notifications API
  - `client.notifications.getContent` to `client.notifications.get_content`
  - `client.notifications.getDraftContent` to `client.notifications.get_draft_content`
  - `client.notifications.getSubmissionChecks` to `client.notifications.get_submission_checks`
  - `client.notifications.putSubmissionChecks` to `client.notifications.put_submission_checks`
  - `client.notifications.deleteSubmissionChecks` to ``client.notifications.delete_submission_checks`

### Removed

- Notifications API
  - `POST /notifications/{notification_id}/variations` with `client.notifications.postVariations` method
  - `POST /notifications/{notification_id}/draft/variations` with `client.notifications.postDraftVariations` method

## [v2.0.0] - 2021-08-23

### Added

- Support for Notifications API by @tk26
  - `GET /notifications` with `client.notifications.list` method
  - `GET /notifications/{notification_id}/content` with `client.notifications.getContent` method
  - `GET /notifications/{notification_id}/draft/content` with `client.notifications.getDraftContent` method
  - `POST /notifications/{notification_id}/variations` with `client.notifications.postVariations` method
  - `POST /notifications/{notification_id}/draft/variations` with `client.notifications.postDraftVariations` method
  - `GET /notifications/{notification_id}/{submission_id}/checks` with `client.notifications.getSubmissionChecks` method
  - `PUT /notifications/{notification_id}/{submission_id}/checks` with `client.notifications.putSubmissionChecks` method
  - `DELETE /notifications/{notification_id}/{submission_id}/checks` with `client.notifications.deleteSubmissionChecks` method

## [v1.9.0] - 2021-06-01

### Added

- Support for Idempotency Key Expiration. You can pass `idempotency_expiration` to the following methods by @andrewmilas10:
  - `send()`
  - `merge_profile()`
  - `create_brand()`

### Updated

- Fix profile -> profiles in README

## [v1.8.0] - 2021-04-07

### Added

- Support for [Automation API](https://docs.courier.com/reference/automation-api) by @tk26
  - `POST /automations/invoke` with `client.automations.invoke` method
  - `POST /automations/{template_id}/invoke` with `client.automations.invoke_template` method

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

[unreleased]: https://github.com/trycourier/courier-python/compare/v4.4.0...HEAD
[v4.4.0]: https://github.com/trycourier/courier-python/compare/v4.3.0...v4.4.0
[v4.3.0]: https://github.com/trycourier/courier-python/compare/v4.2.0...v4.3.0
[v4.2.0]: https://github.com/trycourier/courier-python/compare/v4.1.0...v4.2.0
[v4.1.0]: https://github.com/trycourier/courier-python/compare/v4.0.0...v4.1.0
[v4.0.0]: https://github.com/trycourier/courier-python/compare/v3.0.0...v4.0.0
[v3.0.0]: https://github.com/trycourier/courier-python/compare/v2.0.0...v3.0.0
[v2.0.0]: https://github.com/trycourier/courier-python/compare/v1.9.0...v2.0.0
[v1.9.0]: https://github.com/trycourier/courier-python/compare/v1.8.0...v1.9.0
[v1.8.0]: https://github.com/trycourier/courier-python/compare/v1.7.0...v1.8.0
[v1.7.0]: https://github.com/trycourier/courier-python/compare/v1.6.0...v1.7.0
[v1.6.0]: https://github.com/trycourier/courier-python/compare/v1.5.0...v1.6.0
[v1.5.0]: https://github.com/trycourier/courier-python/compare/v1.4.0...v1.5.0
[v1.4.0]: https://github.com/trycourier/courier-python/compare/v1.3.0...v1.4.0
[v1.3.0]: https://github.com/trycourier/courier-python/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/trycourier/courier-python/compare/v1.1.0...v1.2.0
[v1.1.0]: https://github.com/trycourier/courier-python/compare/v1.0.0...v1.1.0
