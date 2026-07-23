import requests
from typing import Dict, Any, List
from ..config import DATAVERSE_ENV_URL


class DataverseClient:
    """
    Minimal Dataverse client for meeting metadata, agenda, notes, etc.
    """

    def __init__(self, token: str = "<access-token-placeholder>"):
        self.base_url = DATAVERSE_ENV_URL
        self.token = token

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "OData-MaxVersion": "4.0",
            "OData-Version": "4.0",
        }

    def get_meeting_records(self, committee_id: str, period: str) -> List[Dict[str, Any]]:
        """
        period: 'quarterly' | 'halfyearly' | 'annual'
        """
        url = f"{self.base_url}/api/data/v9.2/new_meetings"
        params = {
            "$filter": f"new_committeeid eq '{committee_id}' and new_period eq '{period}'"
        }
        resp = requests.get(url, headers=self._headers(), params=params)
        resp.raise_for_status()
        return resp.json().get("value", [])
