from .exceptions import CourierAPIException


class Bulk():
    key = "bulk"

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    @property
    def uri(self):
        return "%s/%s" % (self.base_url, self.key)

    def create_job(self, message,
                   idempotency_key=None,
                   idempotency_expiration=None):
        """
        Create a new bulk messaging job

        Args:
            message (dict): Job Definition: message
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.
            idempotency_expiration (str, optional): A unique identifier used to
            ensure idempotency of the the request. Passed in the
            x-idempotency-expiration HTTP header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains a jobId
        """
        url = "%s" % self.uri
        headers = {}
        payload = {
            'message': message
        }

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def ingest_users(self, job_id, users,
                     idempotency_key=None,
                     idempotency_expiration=None):
        """
        Ingests users into a bulk processing job

        Args:
            job_id: A job id to ingest users in
            users (list): A list of users to be ingested
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.
            idempotency_expiration (str, optional): A unique identifier used to
            ensure idempotency of the the request. Passed in the
            x-idempotency-expiration HTTP header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains errors if any and total count of users in the job
        """
        url = "%s/%s" % (self.uri, job_id)
        headers = {}
        payload = {
            'users': users
        }

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def run_job(self, job_id,
                idempotency_key=None,
                idempotency_expiration=None):
        """
        Runs a bulk processing job

        Args:
            job_id: A job id to ingest users in
            idempotency_key (str, optional): A unique identifier used to ensure
            idempotency of the the request. Passed in the Idempotency-Key HTTP
            header. Defaults to None.
            idempotency_expiration (str, optional): A unique identifier used to
            ensure idempotency of the the request. Passed in the
            x-idempotency-expiration HTTP header. Defaults to None.

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains status accepted
        """
        url = "%s/%s/run" % (self.uri, job_id)
        headers = {}
        payload = {}

        if idempotency_key:
            headers['Idempotency-Key'] = idempotency_key

        if idempotency_expiration:
            headers['x-idempotency-expiration'] = idempotency_expiration

        resp = self.session.post(url, json=payload, headers=headers)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_job(self, job_id):
        """
        Gets bulk processing job details

        Args:
            job_id: A job id to get the details of

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains job definition
        """
        url = "%s/%s" % (self.uri, job_id)
        resp = self.session.get(url)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()

    def get_job_users(self, job_id, cursor=None):
        """
        Gets bulk processing job user details

        Args:
            job_id: A job id to get the details of
            cursor: optional pointer to for fetching subsequent result pages

        Raises:
            CourierAPIException: Any error returned by the Courier API

        Returns:
            dict: Contains user details and paging info
        """

        params = {}

        if cursor:
            params['cursor'] = cursor

        url = "%s/%s/users" % (self.uri, job_id)
        resp = self.session.get(url, params=params)

        if resp.status_code >= 400:
            raise CourierAPIException(resp)

        return resp.json()
