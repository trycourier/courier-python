# Reference
<details><summary><code>client.<a href="src/courier/client.py">send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the send API to send a message to one or more recipients.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import (
    ContentMessage,
    ElementalContentSugar,
    Routing,
    UserRecipient,
)
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.send(
    message=ContentMessage(
        to=UserRecipient(
            email="email@example.com",
        ),
        content=ElementalContentSugar(
            title="Welcome!",
            body="Thanks for signing up, {{name}}",
        ),
        data={"name": "Peter Parker"},
        routing=Routing(
            method="single",
            channels=["email"],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message:** `Message` — Defines the message to be delivered
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audiences
<details><summary><code>client.audiences.<a href="src/courier/audiences/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified audience by id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audiences.get(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — A unique identifier representing the audience_id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/courier/audiences/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audiences.update(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — A unique identifier representing the audience id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the audience
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the audience
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/courier/audiences/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audiences.delete(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — A unique identifier representing the audience id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/courier/audiences/client.py">list_members</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of members of an audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audiences.list_members(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — A unique identifier representing the audience id
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of members
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/courier/audiences/client.py">list_audiences</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the audiences associated with the authorization token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audiences.list_audiences()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of audiences
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AuditEvents
<details><summary><code>client.audit_events.<a href="src/courier/audit_events/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the list of audit events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audit_events.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of audit events.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audit_events.<a href="src/courier/audit_events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a specific audit event by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.audit_events.get(
    audit_event_id="audit-event-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_event_id:** `str` — A unique identifier associated with the audit event you wish to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AuthTokens
<details><summary><code>client.auth_tokens.<a href="src/courier/auth_tokens/client.py">issue_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a new access token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.auth_tokens.issue_token(
    scope="scope",
    expires_in="expires_in",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scope:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Automations
<details><summary><code>client.automations.<a href="src/courier/automations/client.py">invoke_automation_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invoke an automation run from an automation template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import AutomationInvokeParams
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.automations.invoke_automation_template(
    template_id="templateId",
    request=AutomationInvokeParams(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — A unique identifier representing the automation template to be invoked. This could be the Automation Template ID or the Automation Template Alias.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AutomationInvokeParams` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/courier/automations/client.py">invoke_ad_hoc_automation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invoke an ad hoc automation run. This endpoint accepts a JSON payload with a series of automation steps. For information about what steps are available, checkout the ad hoc automation guide [here](https://www.courier.com/docs/automations/steps/).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import (
    Automation,
    AutomationAdHocInvokeParams,
    AutomationDelayStep,
    AutomationSendStep,
)
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.automations.invoke_ad_hoc_automation(
    request=AutomationAdHocInvokeParams(
        data={"name": "Foo"},
        profile={"tenant_id": "abc-123"},
        recipient="user-yes",
        automation=Automation(
            cancelation_token="delay-send--user-yes--abc-123",
            steps=[
                AutomationDelayStep(
                    until="20240408T080910.123",
                ),
                AutomationSendStep(
                    template="64TP5HKPFTM8VTK1Y75SJDQX9JK0",
                ),
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AutomationAdHocInvokeParams` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Brands
<details><summary><code>client.brands.<a href="src/courier/brands/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import BrandParameters, BrandSettings
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.brands.create(
    request=BrandParameters(
        name="name",
        settings=BrandSettings(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BrandParameters` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.brands.<a href="src/courier/brands/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a specific brand by brand ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.brands.get(
    brand_id="brand_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_id:** `str` — A unique identifier associated with the brand you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.brands.<a href="src/courier/brands/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of brands.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.brands.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of brands.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.brands.<a href="src/courier/brands/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a brand by brand ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.brands.delete(
    brand_id="brand_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_id:** `str` — A unique identifier associated with the brand you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.brands.<a href="src/courier/brands/client.py">replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace an existing brand with the supplied values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.brands.replace(
    brand_id="brand_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_id:** `str` — A unique identifier associated with the brand you wish to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the brand.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[BrandSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**snippets:** `typing.Optional[BrandSnippets]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bulk
<details><summary><code>client.bulk.<a href="src/courier/bulk/client.py">create_job</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import InboundBulkMessage
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.bulk.create_job(
    message=InboundBulkMessage(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message:** `InboundBulkMessage` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk.<a href="src/courier/bulk/client.py">ingest_users</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingest user data into a Bulk Job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import BulkIngestUsersParams, InboundBulkMessageUser
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.bulk.ingest_users(
    job_id="job_id",
    request=BulkIngestUsersParams(
        users=[InboundBulkMessageUser(), InboundBulkMessageUser()],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — A unique identifier representing the bulk job
    
</dd>
</dl>

<dl>
<dd>

**request:** `BulkIngestUsersParams` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk.<a href="src/courier/bulk/client.py">run_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run a bulk job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.bulk.run_job(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — A unique identifier representing the bulk job
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk.<a href="src/courier/bulk/client.py">get_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a bulk job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.bulk.get_job(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — A unique identifier representing the bulk job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk.<a href="src/courier/bulk/client.py">get_users</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Bulk Job Users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.bulk.get_users(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — A unique identifier representing the bulk job
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of users added to the bulk job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Inbound
<details><summary><code>client.inbound.<a href="src/courier/inbound/client.py">track</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import InboundTrackEvent
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.inbound.track(
    request=InboundTrackEvent(
        event="New Order Placed",
        message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
        user_id="1234",
        properties={"order_id": 123, "total_orders": 5, "last_order_id": 122},
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InboundTrackEvent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Lists
<details><summary><code>client.lists.<a href="src/courier/lists/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all of the lists, with the ability to filter based on a pattern.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next page of lists.
    
</dd>
</dl>

<dl>
<dd>

**pattern:** `typing.Optional[str]` — "A pattern used to filter the list items returned. Pattern types supported: exact match on `list_id` or a pattern of one or more pattern parts. you may replace a part with either: `*` to match all parts in that position, or `**` to signify a wildcard `endsWith` pattern match."
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list based on the list ID provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.get(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace an existing list with the supplied values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import ListPutParams
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.update(
    list_id="list_id",
    request=ListPutParams(
        name="name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ListPutParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a list by list ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.delete(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">restore</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a previously deleted list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.restore(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">get_subscribers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list's subscriptions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.get_subscribers(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of list subscriptions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">update_subscribers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes the users to the list, overwriting existing subscriptions. If the list does not exist, it will be automatically created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import PutSubscriptionsRecipient
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.update_subscribers(
    list_id="list_id",
    recipients=[
        PutSubscriptionsRecipient(
            recipient_id="recipientId",
        ),
        PutSubscriptionsRecipient(
            recipient_id="recipientId",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Sequence[PutSubscriptionsRecipient]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">add_subscribers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes additional users to the list, without modifying existing subscriptions. If the list does not exist, it will be automatically created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import PutSubscriptionsRecipient
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.add_subscribers(
    list_id="list_id",
    recipients=[
        PutSubscriptionsRecipient(
            recipient_id="recipientId",
        ),
        PutSubscriptionsRecipient(
            recipient_id="recipientId",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Sequence[PutSubscriptionsRecipient]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">subscribe</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe a user to an existing list (note: if the List does not exist, it will be automatically created).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.subscribe(
    list_id="list_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the recipient associated with the list
    
</dd>
</dl>

<dl>
<dd>

**preferences:** `typing.Optional[RecipientPreferences]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/courier/lists/client.py">unsubscribe</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a subscription to a list by list ID and user ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.lists.unsubscribe(
    list_id="list_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — A unique identifier representing the list you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the recipient associated with the list
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.messages.<a href="src/courier/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the statuses of messages you've previously sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — A boolean value that indicates whether archived messages should be included in the response.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of messages.
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[str]` — A unique identifier representing the event that was used to send the event.
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[str]` — A unique identifier representing the list the message was sent to.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — A unique identifier representing the message_id returned from either /send or /send/list.
    
</dd>
</dl>

<dl>
<dd>

**notification:** `typing.Optional[str]` — A unique identifier representing the notification that was used to send the event.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The key assocated to the provider you want to filter on. E.g., sendgrid, inbox, twilio, slack, msteams, etc. Allows multiple values to be set in query parameters.
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `typing.Optional[str]` — A unique identifier representing the recipient associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — An indicator of the current status of the message. Allows multiple values to be set in query parameters.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A tag placed in the metadata.tags during a notification send. Allows multiple values to be set in query parameters.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — A comma delimited list of 'tags'. Messages will be returned if they match any of the tags passed in.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — Messages sent with the context of a Tenant
    
</dd>
</dl>

<dl>
<dd>

**enqueued_after:** `typing.Optional[str]` — The enqueued datetime of a message to filter out messages received before.
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `typing.Optional[str]` — The unique identifier used to trace the requests
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/courier/messages/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the status of a message you've previously sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.get(
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — A unique identifier associated with the message you wish to retrieve (results from a send).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/courier/messages/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.cancel(
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — A unique identifier representing the message ID
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/courier/messages/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the array of events of a message you've previously sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.get_history(
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — A unique identifier representing the message ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — A supported Message History type that will filter the events returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/courier/messages/client.py">get_content</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.get_content(
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — A unique identifier associated with the message you wish to retrieve (results from a send).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/courier/messages/client.py">archive</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.messages.archive(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` — A unique identifier representing the request ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[bool]` — Retrieve the notes from the Notification template settings.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">get_content</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.get_content(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">get_draft_content</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.get_draft_content(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">get_submission_checks</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.get_submission_checks(
    id="id",
    submission_id="submissionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**submission_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">replace_submission_checks</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import BaseCheck
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.replace_submission_checks(
    id="id",
    submission_id="submissionId",
    checks=[
        BaseCheck(
            id="id",
            status="RESOLVED",
        ),
        BaseCheck(
            id="id",
            status="RESOLVED",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**submission_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**checks:** `typing.Sequence[BaseCheck]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/courier/notifications/client.py">cancel_submission</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.notifications.cancel_submission(
    id="id",
    submission_id="submissionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**submission_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Profiles
<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified user profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.get(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merge the supplied values with an existing profile or create a new profile if one doesn't already exist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.create(
    user_id="user_id",
    profile={"profile": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When using `PUT`, be sure to include all the key-value pairs required by the recipient's profile. 
Any key-value pairs that exist in the profile but fail to be included in the `PUT` request will be 
removed from the profile. Remember, a `PUT` update is a full replacement of the data. For partial updates, 
use the [Patch](https://www.courier.com/docs/reference/profiles/patch/) request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.replace(
    user_id="user_id",
    profile={"profile": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">merge_profile</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import ProfileUpdateRequest, UserProfilePatch
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.merge_profile(
    user_id="user_id",
    request=ProfileUpdateRequest(
        patch=[
            UserProfilePatch(
                op="op",
                path="path",
                value="value",
            ),
            UserProfilePatch(
                op="op",
                path="path",
                value="value",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ProfileUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified user profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">get_list_subscriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the subscribed lists for a specified user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.get_list_subscriptions(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of message statuses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">subscribe_to_lists</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes the given user to one or more lists. If the list does not exist, it will be created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import SubscribeToListsRequest, SubscribeToListsRequestListObject
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.subscribe_to_lists(
    user_id="user_id",
    request=SubscribeToListsRequest(
        lists=[
            SubscribeToListsRequestListObject(
                list_id="listId",
            ),
            SubscribeToListsRequestListObject(
                list_id="listId",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SubscribeToListsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_expiry:** `typing.Optional[str]` — The expiry can either be an ISO8601 datetime or a duration like "1 Day".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/courier/profiles/client.py">delete_list_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes all list subscriptions for given user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.profiles.delete_list_subscription(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier representing the user associated with the requested profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Templates
<details><summary><code>client.templates.<a href="src/courier/templates/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of notification templates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.templates.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A unique identifier that allows for fetching the next set of templates
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants
<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">create_or_replace</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.create_or_replace(
    tenant_id="tenant_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — A unique identifier representing the tenant to be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**parent_tenant_id:** `typing.Optional[str]` — Tenant's parent id (if any).
    
</dd>
</dl>

<dl>
<dd>

**default_preferences:** `typing.Optional[DefaultPreferences]` — Defines the preferences used for the tenant when the user hasn't specified their own.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary properties accessible to a template.
    
</dd>
</dl>

<dl>
<dd>

**user_profile:** `typing.Optional[typing.Dict[str, typing.Any]]` — A user profile object merged with user profile on send.
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `typing.Optional[str]` — Brand to be used for the account when one is not specified by the send call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.get(
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — A unique identifier representing the tenant to be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent_tenant_id:** `typing.Optional[str]` — Filter the list of tenants by parent_id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of tenants to return 
(defaults to 20, maximum value of 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Continue the pagination with the next cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.delete(
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">get_users_by_tenant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.get_users_by_tenant(
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant for user membership.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of accounts to return 
(defaults to 20, maximum value of 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Continue the pagination with the next cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">create_or_replace_default_preferences_for_topic</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import SubscriptionTopicNew
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.create_or_replace_default_preferences_for_topic(
    tenant_id="tenantABC",
    topic_id="HB529N49MD4D5PMX9WR5P4JH78NA",
    request=SubscriptionTopicNew(
        status="OPTED_IN",
        has_custom_routing=True,
        custom_routing=["inbox"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant to update the default preferences for.
    
</dd>
</dl>

<dl>
<dd>

**topic_id:** `str` — Id fo the susbcription topic you want to have a default preference for.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SubscriptionTopicNew` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">remove_default_preferences_for_topic</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.remove_default_preferences_for_topic(
    tenant_id="tenant_id",
    topic_id="topic_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant to update the default preferences for.
    
</dd>
</dl>

<dl>
<dd>

**topic_id:** `str` — Id fo the susbcription topic you want to have a default preference for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">get_template_by_tenant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.get_template_by_tenant(
    tenant_id="tenant_id",
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant for which to retrieve the template.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `str` — Id of the template to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/courier/tenants/client.py">get_template_list_by_tenant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.tenants.get_template_list_by_tenant(
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant for which to retrieve the templates.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of templates to return (defaults to 20, maximum value of 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Continue the pagination with the next cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Translations
<details><summary><code>client.translations.<a href="src/courier/translations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get translations by locale
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.translations.get(
    domain="domain",
    locale="locale",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The domain you want to retrieve translations for. Only `default` is supported at the moment
    
</dd>
</dl>

<dl>
<dd>

**locale:** `str` — The locale you want to retrieve the translations for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translations.<a href="src/courier/translations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a translation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.translations.update(
    domain="domain",
    locale="locale",
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The domain you want to retrieve translations for. Only `default` is supported at the moment
    
</dd>
</dl>

<dl>
<dd>

**locale:** `str` — The locale you want to retrieve the translations for
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Preferences
<details><summary><code>client.users.preferences.<a href="src/courier/users/preferences/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all user preferences.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.preferences.list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier associated with the user whose preferences you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — Query the preferences of a user for this specific tenant context.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.preferences.<a href="src/courier/users/preferences/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch user preferences for a specific subscription topic.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.preferences.get(
    user_id="user_id",
    topic_id="topic_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier associated with the user whose preferences you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**topic_id:** `str` — A unique identifier associated with a subscription topic.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — Query the preferences of a user for this specific tenant context.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.preferences.<a href="src/courier/users/preferences/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update or Create user preferences for a specific subscription topic.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier
from courier.users import TopicPreferenceUpdate

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.preferences.update(
    user_id="abc-123",
    topic_id="74Q4QGFBEX481DP6JRPMV751H4XT",
    topic=TopicPreferenceUpdate(
        status="OPTED_IN",
        has_custom_routing=True,
        custom_routing=["inbox", "email"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — A unique identifier associated with the user whose preferences you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**topic_id:** `str` — A unique identifier associated with a subscription topic.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `TopicPreferenceUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — Update the preferences of a user for this specific tenant context.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Tenants
<details><summary><code>client.users.tenants.<a href="src/courier/users/tenants/client.py">add_multple</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to add a user to
multiple tenants in one call.
A custom profile can also be supplied for each tenant. 
This profile will be merged with the user's main 
profile when sending to the user with that tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier import UserTenantAssociation
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tenants.add_multple(
    user_id="user_id",
    tenants=[
        UserTenantAssociation(
            tenant_id="tenant_id",
        ),
        UserTenantAssociation(
            tenant_id="tenant_id",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**tenants:** `typing.Sequence[UserTenantAssociation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tenants.<a href="src/courier/users/tenants/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to add a single tenant.

A custom profile can also be supplied with the tenant. 
This profile will be merged with the user's main profile 
when sending to the user with that tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tenants.add(
    user_id="user_id",
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Id of the user to be added to the supplied tenant.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant the user should be added to.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tenants.<a href="src/courier/users/tenants/client.py">remove_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a user from any tenants they may have been associated with.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tenants.remove_all(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Id of the user to be removed from the supplied tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tenants.<a href="src/courier/users/tenants/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a user from the supplied tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tenants.remove(
    user_id="user_id",
    tenant_id="tenant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Id of the user to be removed from the supplied tenant.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `str` — Id of the tenant the user should be removed from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tenants.<a href="src/courier/users/tenants/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of user tenant associations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tenants.list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Id of the user to retrieve all associated tenants for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of accounts to return 
(defaults to 20, maximum value of 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Continue the pagination with the next cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Tokens
<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">add_multiple</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds multiple tokens to a user and overwrites matching existing tokens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.add_multiple(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a single token to a user and overwrites a matching existing token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier
from courier.users import UserToken

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.add(
    user_id="user_id",
    token="token",
    request=UserToken(
        provider_key="firebase-fcm",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The full token string.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserToken` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a JSON Patch (RFC 6902) to the specified token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier
from courier.users import PatchOperation, PatchUserTokenOpts

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.update(
    user_id="user_id",
    token="token",
    request=PatchUserTokenOpts(
        patch=[
            PatchOperation(
                op="op",
                path="path",
            ),
            PatchOperation(
                op="op",
                path="path",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The full token string.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchUserTokenOpts` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get single token available for a `:token`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.get(
    user_id="user_id",
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The full token string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all tokens available for a :user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.tokens.<a href="src/courier/users/tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from courier.client import Courier

client = Courier(
    authorization_token="YOUR_AUTHORIZATION_TOKEN",
)
client.users.tokens.delete(
    user_id="user_id",
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user's ID. This can be any uniquely identifiable string.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The full token string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

