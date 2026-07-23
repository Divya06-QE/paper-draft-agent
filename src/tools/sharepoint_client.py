import requests
from typing import Dict, Any, List
from ..config import SHAREPOINT_SITE_URL, SHAREPOINT_DOC_LIB, TENANT_ID, CLIENT_ID, CLIENT_SECRET


class SharePointClient:
    """
    Minimal SharePoint client using client credentials.
    Replace token acquisition with MSAL or Graph SDK in production.
    """

    def __init__(self):
        self.site_url = SHAREPOINT_SITE_URL
        self.doc_lib = SHAREPOINT_DOC_LIB
        self._token = self._get_token()

    def _get_token(self) -> str:
        # Placeholder: implement proper OAuth2 / MSAL token acquisition
        return "<access-token-placeholder>"

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/json;odata=verbose",
        }

    def get_previous_papers(self, committee_id: str) -> List[Dict[str, Any]]:
        # Example: query by metadata field CommitteeId
        url = f"{self.site_url}/_api/web/lists/getbytitle('{self.doc_lib}')/items"
        params = {"$filter": f"CommitteeId eq '{committee_id}'"}
        resp = requests.get(url, headers=self._headers(), params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("d", {}).get("results", [])

    def save_draft(self, user_upn: str, committee_id: str, file_name: str, content: str) -> str:
        """
        Save draft to user-specific folder, e.g. /Drafts/<user>/<committee>/<file>.
        Returns the file URL.
        """
        # Placeholder: implement upload via SharePoint REST or Graph API
        file_url = f"{self.site_url}/Drafts/{user_upn}/{committee_id}/{file_name}"
        # Upload logic omitted
        return file_url
