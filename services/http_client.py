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
