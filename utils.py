from __future__ import annotations

import os
from typing import Any

import requests


def _get_api_key() -> str:
    api_key = os.getenv("SPLITWISE_OAUTH2_API_KEY")
    if api_key is None:
        raise RuntimeError("SPLITWISE_OAUTH2_API_KEY is missing from the .env file.")
    return api_key


def _make_request(
    url: str,
    method: str,
    api_key: str = "",
    data: dict[str, Any] = None,
    params: dict[str, Any] = None,
) -> requests.Response:
    headers = {}
    if api_key:
        headers = {"Authorization": f"Bearer {api_key}"}

    request_object = requests.Request(method=method, url=url, headers=headers, data=data, params=params)
    prepped_request = request_object.prepare()
    with requests.Session() as session:
        response = session.send(request=prepped_request)
        return response
