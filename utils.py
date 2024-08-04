from __future__ import annotations

from functools import lru_cache
from typing import Any

import requests
from fastapi import HTTPException

from config import settings


@lru_cache
def _get_api_key() -> str:
    api_key = settings.splitwise_oauth2_api_key
    if api_key is None:
        raise RuntimeError("SPLITWISE_OAUTH2_API_KEY is missing from the .env file.")
    return api_key


def _make_request(
    url: str,
    method: str,
    data: dict[str, Any] = None,
    params: dict[str, Any] = None,
    headers: dict[str, Any] = None,
) -> requests.Response:
    api_key = _get_api_key()
    headers = {"Authorization": f"Bearer {api_key}"}
    if headers:
        headers.update(headers)

    request_object = requests.Request(method=method, url=url, headers=headers, data=data, params=params)
    prepped_request = request_object.prepare()
    with requests.Session() as session:
        response = session.send(request=prepped_request)
        if response.ok:
            return response
        _handle_request(response=response)


def _handle_request(response: requests.Response) -> None:
    if response.status_code == 401:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    response.raise_for_status()
