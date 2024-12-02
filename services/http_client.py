from typing import Any

from playwright.sync_api import APIRequestContext
from playwright.sync_api._generated import APIResponse

from config.config import TIMEOUT
from utils.allure_utils import AllureUtils


class HTTPClient:
    """HTTP client for making requests to a specified base URL."""

    def __init__(self, api_context: APIRequestContext) -> None:
        """Initializes the HTTPClient with APIRequestContext."""
        self.api_request_context: APIRequestContext = api_context

    def get(
        self,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Sends a GET request to the specified endpoint with the provided data."""
        response: APIResponse = self.api_request_context.get(
            endpoint, headers=headers, params=params, timeout=TIMEOUT
        )
        AllureUtils.attach_response(response)
        return response

    def delete(
        self,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Sends a DELETE request to the specified endpoint with the provided data."""
        response: APIResponse = self.api_request_context.delete(
            endpoint, headers=headers, params=params, timeout=TIMEOUT
        )
        AllureUtils.attach_response(response)
        return response

    def post(
        self,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Sends a POST request to the specified endpoint with the provided data."""
        kwargs = {}
        if headers:
            kwargs["headers"] = headers

        if json is not None:
            kwargs["data"] = json
        elif data is not None:
            kwargs["data"] = data

        response: APIResponse = self.api_request_context.post(
            endpoint, **kwargs, timeout=TIMEOUT
        )
        AllureUtils.attach_response(response)
        return response

    def put(
        self,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Sends a PUT request to the specified endpoint with the provided data."""
        response: APIResponse = self.api_request_context.put(
            endpoint, headers=headers, json=json, data=data, timeout=TIMEOUT
        )
        AllureUtils.attach_response(response)
        return response

    def patch(
        self,
        endpoint: str,
        headers: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Sends a PATCH request to the specified endpoint with the provided data."""
        response: APIResponse = self.api_request_context.patch(
            endpoint, headers=headers, data=json or data, timeout=TIMEOUT
        )
        AllureUtils.attach_response(response)
        return response
