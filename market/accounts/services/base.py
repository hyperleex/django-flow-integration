import httpx
from djangorestframework_camel_case.util import underscoreize

from utils.url import get_full_url


class ServiceError(Exception):
    ...


class RetryError(Exception):
    ...


class BaseFlowService:
    def __init__(self):
        self.base_url = "http://api:3000/v1/"
        self.client = httpx.Client(transport=httpx.HTTPTransport(retries=5))

    def _send_request(self, method, url_path, **kwargs):
        """
        Send real request with retries if service temporarily unavailable
        """
        url = get_full_url(base_url=self.base_url, url_path=url_path)
        retry_number = 5
        while retry_number > 0:
            response = self.client.request(method, url, **kwargs)
            if 200 <= response.status_code < 300:
                return underscoreize(response.json())
            if 400 <= response.status_code < 500:
                raise ServiceError()
            if response.status_code >= 500:
                retry_number -= 1
        raise RetryError
