from .exceptions import CourierAPIException


class Automations():
    key = "automations"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def invoke(self, automation, brand=None, data=None,
               profile=None, recipient=None, template=None):
        """
        Invoke an ad-hoc automation

        Args:
            automation (dict): An object that includes steps (bare minimum) to
            be executed on invoke.
            brand (str, optional): A unique identifier that represents the
            brand that should be used for rendering the notification.
            Defaults to None.
            data (dict, optional): An object that includes any data you want to
            pass to a message template. Defaults to None.
            profile (dict, optional): Any key-value pairs required by your
            chosen Integrations. Defaults to None.
            recipient (str, optional): A unique identifier associated with the
            recipient of the delivered message. Defaults to None.
            template (str, optional): A unique identifier that can be mapped to
            an individual Notification. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a runId
        """

        url = "%s/automations/invoke" % self.base_url
        headers = {}
        payload = {
            'automation': automation
        }

        if brand:
            payload['brand'] = brand

        if data:
            payload['data'] = data

        if profile:
            payload['profile'] = profile

        if recipient:
            payload['recipient'] = recipient

        if template:
            payload['template'] = template

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def invoke_template(self, template_id, brand=None, data=None,
                        profile=None, recipient=None, template=None):
        """
        Invoke an automation template

        Args:
            template_id (str): A unique identifier that represents the
            automation template to be invoked.
            brand (str, optional): A unique identifier that represents the
            brand that should be used for rendering the notification.
            Defaults to None.
            data (dict, optional): An object that includes any data you want to
            pass to a message template. Defaults to None.
            profile (dict, optional): Any key-value pairs required by your
            chosen Integrations. Defaults to None.
            recipient (str, optional): A unique identifier associated with the
            recipient of the delivered message. Defaults to None.
            template (str, optional): A unique identifier that can be mapped to
            an individual Notification. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a runId
        """

        url = "%s/automations/%s/invoke" % (self.base_url, template_id)
        headers = {}
        payload = {}

        if brand:
            payload['brand'] = brand

        if data:
            payload['data'] = data

        if profile:
            payload['profile'] = profile

        if recipient:
            payload['recipient'] = recipient

        if template:
            payload['template'] = template

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
