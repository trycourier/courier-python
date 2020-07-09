# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [v1.3.0] - 2020-07-09

### Added
- Support for [Brands API](https://docs.trycourier.com/reference/brands-api) by @aydrian
  - `GET /brands` with `get_brands` method
  - `GET /brands/:brand_id` with `get_brand` method
  - `POST /brands` with `create_brand` method
  - `PUT /brands/:brand_id` with `replace_brand` method
  - `DELETE /brands/:brand_id` with `delete_brand` method
- Support for specifying notification brand during [send](https://docs.trycourier.com/reference/send-api#sendmessage) by @aydrian

### Changed
- Updated [requests](https://pypi.org/project/requests/) library to v2.24.0

## [v1.2.0] - 2020-06-18

### Added

- Support for [`GET /messages/{message_id}`](https://docs.trycourier.com/reference/messages-api#getmessagebyid) with `get_message` method by @jackwestmoretab (Thank you! :tada:)
- Support for [`GET /messages`](https://docs.trycourier.com/reference/messages-api#getmessages) with `get_messages` method by @aydrian
- Support for [Events API](https://docs.trycourier.com/reference/events-api) with `get_events`, `get_event`, and `replace_event` methods by @aydrian

## [v1.1.0] - 2020-03-20

### Added

- Support for [Profiles API](https://docs.trycourier.com/reference/profiles-api) with `get_profile`, `replace_profile`, and `merge_profile` methods by @aydrian

## v1.0.0 - 2020-03-06

Initial release. Supports Python 3.5+. Supports Send API.

[v1.3.0]: https://github.com/trycourier/courier-python/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/trycourier/courier-python/compare/v1.1.0...v1.2.0
[v1.1.0]: https://github.com/trycourier/courier-python/compare/v1.0.0...v1.1.0
