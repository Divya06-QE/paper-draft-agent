import requests
from typing import Dict, Any
from ..config import POWER_PLATFORM_FLOW_URL


class PowerPlatformClient:
    """
    Example client to trigger a Power Automate flow for additional enrichment or logging.
    """

    def trigger_flow(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        resp = requests.post(POWER_PLATFORM_FLOW_URL, json=payload)
        resp.raise_for_status()
        return resp.json() if resp.content else {}
