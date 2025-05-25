from __future__ import annotations

import requests

from cloudflare.models import GetZonesResponse, ZoneEntity
from configuration.config import get_config

BASE_URL = "https://api.cloudflare.com/client/v4"


def get_zones() -> list[ZoneEntity]:
    url = f"{BASE_URL}/zones"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_token()}",
    }

    response = requests.get(url, headers=headers, timeout=10)

    response.raise_for_status()

    validated_response = GetZonesResponse.model_validate_json(response.content)
    return validated_response.result


def get_api_token() -> str:
    config = get_config()
    cloudflare_config = config["cloudflare"]
    return cloudflare_config["api_token"]
