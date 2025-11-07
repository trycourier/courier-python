# Shared Types

```python
from courier.types import (
    Alignment,
    ChannelClassification,
    ChannelPreference,
    ElementalActionNodeWithType,
    ElementalBaseNode,
    ElementalChannelNode,
    ElementalChannelNodeWithType,
    ElementalContent,
    ElementalContentSugar,
    ElementalDividerNodeWithType,
    ElementalImageNodeWithType,
    ElementalMetaNodeWithType,
    ElementalNode,
    ElementalQuoteNodeWithType,
    ElementalTextNodeWithType,
    MessageContext,
    MessageRouting,
    MessageRoutingChannel,
    NotificationPreferenceDetails,
    Paging,
    Preference,
    PreferenceStatus,
    Recipient,
    RecipientPreferences,
    Rule,
    TextStyle,
    UserRecipient,
    Utm,
)
```

# Send

Types:

```python
from courier.types import SendMessageResponse
```

Methods:

- <code title="post /send">client.send.<a href="./src/courier/resources/send.py">message</a>(\*\*<a href="src/courier/types/send_message_params.py">params</a>) -> <a href="./src/courier/types/send_message_response.py">SendMessageResponse</a></code>

# Audiences

Types:

```python
from courier.types import (
    Audience,
    Filter,
    FilterConfig,
    AudienceUpdateResponse,
    AudienceListResponse,
    AudienceListMembersResponse,
)
```

Methods:

- <code title="get /audiences/{audience_id}">client.audiences.<a href="./src/courier/resources/audiences.py">retrieve</a>(audience_id) -> <a href="./src/courier/types/audience.py">Audience</a></code>
- <code title="put /audiences/{audience_id}">client.audiences.<a href="./src/courier/resources/audiences.py">update</a>(audience_id, \*\*<a href="src/courier/types/audience_update_params.py">params</a>) -> <a href="./src/courier/types/audience_update_response.py">AudienceUpdateResponse</a></code>
- <code title="get /audiences">client.audiences.<a href="./src/courier/resources/audiences.py">list</a>(\*\*<a href="src/courier/types/audience_list_params.py">params</a>) -> <a href="./src/courier/types/audience_list_response.py">AudienceListResponse</a></code>
- <code title="delete /audiences/{audience_id}">client.audiences.<a href="./src/courier/resources/audiences.py">delete</a>(audience_id) -> None</code>
- <code title="get /audiences/{audience_id}/members">client.audiences.<a href="./src/courier/resources/audiences.py">list_members</a>(audience_id, \*\*<a href="src/courier/types/audience_list_members_params.py">params</a>) -> <a href="./src/courier/types/audience_list_members_response.py">AudienceListMembersResponse</a></code>

# AuditEvents

Types:

```python
from courier.types import AuditEvent, AuditEventListResponse
```

Methods:

- <code title="get /audit-events/{audit-event-id}">client.audit_events.<a href="./src/courier/resources/audit_events.py">retrieve</a>(audit_event_id) -> <a href="./src/courier/types/audit_event.py">AuditEvent</a></code>
- <code title="get /audit-events">client.audit_events.<a href="./src/courier/resources/audit_events.py">list</a>(\*\*<a href="src/courier/types/audit_event_list_params.py">params</a>) -> <a href="./src/courier/types/audit_event_list_response.py">AuditEventListResponse</a></code>

# Auth

Types:

```python
from courier.types import AuthIssueTokenResponse
```

Methods:

- <code title="post /auth/issue-token">client.auth.<a href="./src/courier/resources/auth.py">issue_token</a>(\*\*<a href="src/courier/types/auth_issue_token_params.py">params</a>) -> <a href="./src/courier/types/auth_issue_token_response.py">AuthIssueTokenResponse</a></code>

# Automations

Types:

```python
from courier.types import AutomationInvokeResponse
```

## Invoke

Methods:

- <code title="post /automations/invoke">client.automations.invoke.<a href="./src/courier/resources/automations/invoke.py">invoke_ad_hoc</a>(\*\*<a href="src/courier/types/automations/invoke_invoke_ad_hoc_params.py">params</a>) -> <a href="./src/courier/types/automation_invoke_response.py">AutomationInvokeResponse</a></code>
- <code title="post /automations/{templateId}/invoke">client.automations.invoke.<a href="./src/courier/resources/automations/invoke.py">invoke_by_template</a>(template_id, \*\*<a href="src/courier/types/automations/invoke_invoke_by_template_params.py">params</a>) -> <a href="./src/courier/types/automation_invoke_response.py">AutomationInvokeResponse</a></code>

# Brands

Types:

```python
from courier.types import (
    Brand,
    BrandColors,
    BrandSettings,
    BrandSettingsEmail,
    BrandSettingsInApp,
    BrandSnippet,
    BrandSnippets,
    BrandTemplate,
    EmailFooter,
    EmailHead,
    EmailHeader,
    Icons,
    Logo,
    WidgetBackground,
    BrandListResponse,
)
```

Methods:

- <code title="post /brands">client.brands.<a href="./src/courier/resources/brands.py">create</a>(\*\*<a href="src/courier/types/brand_create_params.py">params</a>) -> <a href="./src/courier/types/brand.py">Brand</a></code>
- <code title="get /brands/{brand_id}">client.brands.<a href="./src/courier/resources/brands.py">retrieve</a>(brand_id) -> <a href="./src/courier/types/brand.py">Brand</a></code>
- <code title="put /brands/{brand_id}">client.brands.<a href="./src/courier/resources/brands.py">update</a>(brand_id, \*\*<a href="src/courier/types/brand_update_params.py">params</a>) -> <a href="./src/courier/types/brand.py">Brand</a></code>
- <code title="get /brands">client.brands.<a href="./src/courier/resources/brands.py">list</a>(\*\*<a href="src/courier/types/brand_list_params.py">params</a>) -> <a href="./src/courier/types/brand_list_response.py">BrandListResponse</a></code>
- <code title="delete /brands/{brand_id}">client.brands.<a href="./src/courier/resources/brands.py">delete</a>(brand_id) -> None</code>

# Bulk

Types:

```python
from courier.types import (
    InboundBulkMessage,
    InboundBulkMessageUser,
    BulkCreateJobResponse,
    BulkListUsersResponse,
    BulkRetrieveJobResponse,
)
```

Methods:

- <code title="post /bulk/{job_id}">client.bulk.<a href="./src/courier/resources/bulk.py">add_users</a>(job_id, \*\*<a href="src/courier/types/bulk_add_users_params.py">params</a>) -> None</code>
- <code title="post /bulk">client.bulk.<a href="./src/courier/resources/bulk.py">create_job</a>(\*\*<a href="src/courier/types/bulk_create_job_params.py">params</a>) -> <a href="./src/courier/types/bulk_create_job_response.py">BulkCreateJobResponse</a></code>
- <code title="get /bulk/{job_id}/users">client.bulk.<a href="./src/courier/resources/bulk.py">list_users</a>(job_id, \*\*<a href="src/courier/types/bulk_list_users_params.py">params</a>) -> <a href="./src/courier/types/bulk_list_users_response.py">BulkListUsersResponse</a></code>
- <code title="get /bulk/{job_id}">client.bulk.<a href="./src/courier/resources/bulk.py">retrieve_job</a>(job_id) -> <a href="./src/courier/types/bulk_retrieve_job_response.py">BulkRetrieveJobResponse</a></code>
- <code title="post /bulk/{job_id}/run">client.bulk.<a href="./src/courier/resources/bulk.py">run_job</a>(job_id) -> None</code>

# Inbound

Types:

```python
from courier.types import InboundTrackEventResponse
```

Methods:

- <code title="post /inbound/courier">client.inbound.<a href="./src/courier/resources/inbound.py">track_event</a>(\*\*<a href="src/courier/types/inbound_track_event_params.py">params</a>) -> <a href="./src/courier/types/inbound_track_event_response.py">InboundTrackEventResponse</a></code>

# Lists

Types:

```python
from courier.types import PutSubscriptionsRecipient, SubscriptionList, ListListResponse
```

Methods:

- <code title="get /lists/{list_id}">client.lists.<a href="./src/courier/resources/lists/lists.py">retrieve</a>(list_id) -> <a href="./src/courier/types/subscription_list.py">SubscriptionList</a></code>
- <code title="put /lists/{list_id}">client.lists.<a href="./src/courier/resources/lists/lists.py">update</a>(list_id, \*\*<a href="src/courier/types/list_update_params.py">params</a>) -> None</code>
- <code title="get /lists">client.lists.<a href="./src/courier/resources/lists/lists.py">list</a>(\*\*<a href="src/courier/types/list_list_params.py">params</a>) -> <a href="./src/courier/types/list_list_response.py">ListListResponse</a></code>
- <code title="delete /lists/{list_id}">client.lists.<a href="./src/courier/resources/lists/lists.py">delete</a>(list_id) -> None</code>
- <code title="put /lists/{list_id}/restore">client.lists.<a href="./src/courier/resources/lists/lists.py">restore</a>(list_id) -> None</code>

## Subscriptions

Types:

```python
from courier.types.lists import SubscriptionListResponse
```

Methods:

- <code title="get /lists/{list_id}/subscriptions">client.lists.subscriptions.<a href="./src/courier/resources/lists/subscriptions.py">list</a>(list_id, \*\*<a href="src/courier/types/lists/subscription_list_params.py">params</a>) -> <a href="./src/courier/types/lists/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="post /lists/{list_id}/subscriptions">client.lists.subscriptions.<a href="./src/courier/resources/lists/subscriptions.py">add</a>(list_id, \*\*<a href="src/courier/types/lists/subscription_add_params.py">params</a>) -> None</code>
- <code title="put /lists/{list_id}/subscriptions">client.lists.subscriptions.<a href="./src/courier/resources/lists/subscriptions.py">subscribe</a>(list_id, \*\*<a href="src/courier/types/lists/subscription_subscribe_params.py">params</a>) -> None</code>
- <code title="put /lists/{list_id}/subscriptions/{user_id}">client.lists.subscriptions.<a href="./src/courier/resources/lists/subscriptions.py">subscribe_user</a>(user_id, \*, list_id, \*\*<a href="src/courier/types/lists/subscription_subscribe_user_params.py">params</a>) -> None</code>
- <code title="delete /lists/{list_id}/subscriptions/{user_id}">client.lists.subscriptions.<a href="./src/courier/resources/lists/subscriptions.py">unsubscribe_user</a>(user_id, \*, list_id) -> None</code>

# Messages

Types:

```python
from courier.types import (
    MessageDetails,
    MessageRetrieveResponse,
    MessageListResponse,
    MessageContentResponse,
    MessageHistoryResponse,
)
```

Methods:

- <code title="get /messages/{message_id}">client.messages.<a href="./src/courier/resources/messages.py">retrieve</a>(message_id) -> <a href="./src/courier/types/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /messages">client.messages.<a href="./src/courier/resources/messages.py">list</a>(\*\*<a href="src/courier/types/message_list_params.py">params</a>) -> <a href="./src/courier/types/message_list_response.py">MessageListResponse</a></code>
- <code title="post /messages/{message_id}/cancel">client.messages.<a href="./src/courier/resources/messages.py">cancel</a>(message_id) -> <a href="./src/courier/types/message_details.py">MessageDetails</a></code>
- <code title="get /messages/{message_id}/output">client.messages.<a href="./src/courier/resources/messages.py">content</a>(message_id) -> <a href="./src/courier/types/message_content_response.py">MessageContentResponse</a></code>
- <code title="get /messages/{message_id}/history">client.messages.<a href="./src/courier/resources/messages.py">history</a>(message_id, \*\*<a href="src/courier/types/message_history_params.py">params</a>) -> <a href="./src/courier/types/message_history_response.py">MessageHistoryResponse</a></code>

# Requests

Methods:

- <code title="put /requests/{request_id}/archive">client.requests.<a href="./src/courier/resources/requests.py">archive</a>(request_id) -> None</code>

# Notifications

Types:

```python
from courier.types import BaseCheck, Check, NotificationGetContent, NotificationListResponse
```

Methods:

- <code title="get /notifications">client.notifications.<a href="./src/courier/resources/notifications/notifications.py">list</a>(\*\*<a href="src/courier/types/notification_list_params.py">params</a>) -> <a href="./src/courier/types/notification_list_response.py">NotificationListResponse</a></code>
- <code title="get /notifications/{id}/content">client.notifications.<a href="./src/courier/resources/notifications/notifications.py">retrieve_content</a>(id) -> <a href="./src/courier/types/notification_get_content.py">NotificationGetContent</a></code>

## Draft

Methods:

- <code title="get /notifications/{id}/draft/content">client.notifications.draft.<a href="./src/courier/resources/notifications/draft.py">retrieve_content</a>(id) -> <a href="./src/courier/types/notification_get_content.py">NotificationGetContent</a></code>

## Checks

Types:

```python
from courier.types.notifications import CheckUpdateResponse, CheckListResponse
```

Methods:

- <code title="put /notifications/{id}/{submissionId}/checks">client.notifications.checks.<a href="./src/courier/resources/notifications/checks.py">update</a>(submission_id, \*, id, \*\*<a href="src/courier/types/notifications/check_update_params.py">params</a>) -> <a href="./src/courier/types/notifications/check_update_response.py">CheckUpdateResponse</a></code>
- <code title="get /notifications/{id}/{submissionId}/checks">client.notifications.checks.<a href="./src/courier/resources/notifications/checks.py">list</a>(submission_id, \*, id) -> <a href="./src/courier/types/notifications/check_list_response.py">CheckListResponse</a></code>
- <code title="delete /notifications/{id}/{submissionId}/checks">client.notifications.checks.<a href="./src/courier/resources/notifications/checks.py">delete</a>(submission_id, \*, id) -> None</code>

# Profiles

Types:

```python
from courier.types import (
    SubscribeToListsRequestItem,
    ProfileCreateResponse,
    ProfileRetrieveResponse,
    ProfileReplaceResponse,
)
```

Methods:

- <code title="post /profiles/{user_id}">client.profiles.<a href="./src/courier/resources/profiles/profiles.py">create</a>(user_id, \*\*<a href="src/courier/types/profile_create_params.py">params</a>) -> <a href="./src/courier/types/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="get /profiles/{user_id}">client.profiles.<a href="./src/courier/resources/profiles/profiles.py">retrieve</a>(user_id) -> <a href="./src/courier/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="patch /profiles/{user_id}">client.profiles.<a href="./src/courier/resources/profiles/profiles.py">update</a>(user_id, \*\*<a href="src/courier/types/profile_update_params.py">params</a>) -> None</code>
- <code title="delete /profiles/{user_id}">client.profiles.<a href="./src/courier/resources/profiles/profiles.py">delete</a>(user_id) -> None</code>
- <code title="put /profiles/{user_id}">client.profiles.<a href="./src/courier/resources/profiles/profiles.py">replace</a>(user_id, \*\*<a href="src/courier/types/profile_replace_params.py">params</a>) -> <a href="./src/courier/types/profile_replace_response.py">ProfileReplaceResponse</a></code>

## Lists

Types:

```python
from courier.types.profiles import ListRetrieveResponse, ListDeleteResponse, ListSubscribeResponse
```

Methods:

- <code title="get /profiles/{user_id}/lists">client.profiles.lists.<a href="./src/courier/resources/profiles/lists.py">retrieve</a>(user_id, \*\*<a href="src/courier/types/profiles/list_retrieve_params.py">params</a>) -> <a href="./src/courier/types/profiles/list_retrieve_response.py">ListRetrieveResponse</a></code>
- <code title="delete /profiles/{user_id}/lists">client.profiles.lists.<a href="./src/courier/resources/profiles/lists.py">delete</a>(user_id) -> <a href="./src/courier/types/profiles/list_delete_response.py">ListDeleteResponse</a></code>
- <code title="post /profiles/{user_id}/lists">client.profiles.lists.<a href="./src/courier/resources/profiles/lists.py">subscribe</a>(user_id, \*\*<a href="src/courier/types/profiles/list_subscribe_params.py">params</a>) -> <a href="./src/courier/types/profiles/list_subscribe_response.py">ListSubscribeResponse</a></code>

# Tenants

Types:

```python
from courier.types import (
    BaseTemplateTenantAssociation,
    DefaultPreferences,
    SubscriptionTopicNew,
    Tenant,
    TenantAssociation,
    TenantListResponse,
    TenantListUsersResponse,
)
```

Methods:

- <code title="get /tenants/{tenant_id}">client.tenants.<a href="./src/courier/resources/tenants/tenants.py">retrieve</a>(tenant_id) -> <a href="./src/courier/types/tenant.py">Tenant</a></code>
- <code title="put /tenants/{tenant_id}">client.tenants.<a href="./src/courier/resources/tenants/tenants.py">update</a>(tenant_id, \*\*<a href="src/courier/types/tenant_update_params.py">params</a>) -> <a href="./src/courier/types/tenant.py">Tenant</a></code>
- <code title="get /tenants">client.tenants.<a href="./src/courier/resources/tenants/tenants.py">list</a>(\*\*<a href="src/courier/types/tenant_list_params.py">params</a>) -> <a href="./src/courier/types/tenant_list_response.py">TenantListResponse</a></code>
- <code title="delete /tenants/{tenant_id}">client.tenants.<a href="./src/courier/resources/tenants/tenants.py">delete</a>(tenant_id) -> None</code>
- <code title="get /tenants/{tenant_id}/users">client.tenants.<a href="./src/courier/resources/tenants/tenants.py">list_users</a>(tenant_id, \*\*<a href="src/courier/types/tenant_list_users_params.py">params</a>) -> <a href="./src/courier/types/tenant_list_users_response.py">TenantListUsersResponse</a></code>

## Preferences

### Items

Methods:

- <code title="put /tenants/{tenant_id}/default_preferences/items/{topic_id}">client.tenants.preferences.items.<a href="./src/courier/resources/tenants/preferences/items.py">update</a>(topic_id, \*, tenant_id, \*\*<a href="src/courier/types/tenants/preferences/item_update_params.py">params</a>) -> None</code>
- <code title="delete /tenants/{tenant_id}/default_preferences/items/{topic_id}">client.tenants.preferences.items.<a href="./src/courier/resources/tenants/preferences/items.py">delete</a>(topic_id, \*, tenant_id) -> None</code>

## Templates

Types:

```python
from courier.types.tenants import TemplateListResponse
```

Methods:

- <code title="get /tenants/{tenant_id}/templates/{template_id}">client.tenants.templates.<a href="./src/courier/resources/tenants/templates.py">retrieve</a>(template_id, \*, tenant_id) -> <a href="./src/courier/types/base_template_tenant_association.py">BaseTemplateTenantAssociation</a></code>
- <code title="get /tenants/{tenant_id}/templates">client.tenants.templates.<a href="./src/courier/resources/tenants/templates.py">list</a>(tenant_id, \*\*<a href="src/courier/types/tenants/template_list_params.py">params</a>) -> <a href="./src/courier/types/tenants/template_list_response.py">TemplateListResponse</a></code>

# Translations

Types:

```python
from courier.types import TranslationRetrieveResponse
```

Methods:

- <code title="get /translations/{domain}/{locale}">client.translations.<a href="./src/courier/resources/translations.py">retrieve</a>(locale, \*, domain) -> str</code>
- <code title="put /translations/{domain}/{locale}">client.translations.<a href="./src/courier/resources/translations.py">update</a>(locale, \*, domain, \*\*<a href="src/courier/types/translation_update_params.py">params</a>) -> None</code>

# Users

## Preferences

Types:

```python
from courier.types.users import (
    TopicPreference,
    PreferenceRetrieveResponse,
    PreferenceRetrieveTopicResponse,
    PreferenceUpdateOrCreateTopicResponse,
)
```

Methods:

- <code title="get /users/{user_id}/preferences">client.users.preferences.<a href="./src/courier/resources/users/preferences.py">retrieve</a>(user_id, \*\*<a href="src/courier/types/users/preference_retrieve_params.py">params</a>) -> <a href="./src/courier/types/users/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="get /users/{user_id}/preferences/{topic_id}">client.users.preferences.<a href="./src/courier/resources/users/preferences.py">retrieve_topic</a>(topic_id, \*, user_id, \*\*<a href="src/courier/types/users/preference_retrieve_topic_params.py">params</a>) -> <a href="./src/courier/types/users/preference_retrieve_topic_response.py">PreferenceRetrieveTopicResponse</a></code>
- <code title="put /users/{user_id}/preferences/{topic_id}">client.users.preferences.<a href="./src/courier/resources/users/preferences.py">update_or_create_topic</a>(topic_id, \*, user_id, \*\*<a href="src/courier/types/users/preference_update_or_create_topic_params.py">params</a>) -> <a href="./src/courier/types/users/preference_update_or_create_topic_response.py">PreferenceUpdateOrCreateTopicResponse</a></code>

## Tenants

Types:

```python
from courier.types.users import TenantListResponse
```

Methods:

- <code title="get /users/{user_id}/tenants">client.users.tenants.<a href="./src/courier/resources/users/tenants.py">list</a>(user_id, \*\*<a href="src/courier/types/users/tenant_list_params.py">params</a>) -> <a href="./src/courier/types/users/tenant_list_response.py">TenantListResponse</a></code>
- <code title="put /users/{user_id}/tenants">client.users.tenants.<a href="./src/courier/resources/users/tenants.py">add_multiple</a>(user_id, \*\*<a href="src/courier/types/users/tenant_add_multiple_params.py">params</a>) -> None</code>
- <code title="put /users/{user_id}/tenants/{tenant_id}">client.users.tenants.<a href="./src/courier/resources/users/tenants.py">add_single</a>(tenant_id, \*, user_id, \*\*<a href="src/courier/types/users/tenant_add_single_params.py">params</a>) -> None</code>
- <code title="delete /users/{user_id}/tenants">client.users.tenants.<a href="./src/courier/resources/users/tenants.py">remove_all</a>(user_id) -> None</code>
- <code title="delete /users/{user_id}/tenants/{tenant_id}">client.users.tenants.<a href="./src/courier/resources/users/tenants.py">remove_single</a>(tenant_id, \*, user_id) -> None</code>

## Tokens

Types:

```python
from courier.types.users import UserToken, TokenRetrieveResponse, TokenListResponse
```

Methods:

- <code title="get /users/{user_id}/tokens/{token}">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">retrieve</a>(token, \*, user_id) -> <a href="./src/courier/types/users/token_retrieve_response.py">TokenRetrieveResponse</a></code>
- <code title="patch /users/{user_id}/tokens/{token}">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">update</a>(token, \*, user_id, \*\*<a href="src/courier/types/users/token_update_params.py">params</a>) -> None</code>
- <code title="get /users/{user_id}/tokens">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">list</a>(user_id) -> <a href="./src/courier/types/users/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /users/{user_id}/tokens/{token}">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">delete</a>(token, \*, user_id) -> None</code>
- <code title="put /users/{user_id}/tokens">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">add_multiple</a>(user_id) -> None</code>
- <code title="put /users/{user_id}/tokens/{token}">client.users.tokens.<a href="./src/courier/resources/users/tokens.py">add_single</a>(path_token, \*, user_id, \*\*<a href="src/courier/types/users/token_add_single_params.py">params</a>) -> None</code>
