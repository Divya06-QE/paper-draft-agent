import os
from dotenv import load_dotenv

load_dotenv()

FOUNDRY_PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
FOUNDRY_MODEL_NAME = os.getenv("FOUNDRY_MODEL_NAME")

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SHAREPOINT_SITE_URL = os.getenv("SHAREPOINT_SITE_URL")
SHAREPOINT_DOC_LIB = os.getenv("SHAREPOINT_DOC_LIB")

DATAVERSE_ENV_URL = os.getenv("DATAVERSE_ENV_URL")
POWER_PLATFORM_FLOW_URL = os.getenv("POWER_PLATFORM_FLOW_URL")

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
OUTLOOK_SENDER_ADDRESS = os.getenv("OUTLOOK_SENDER_ADDRESS")

COMMITTEE_CONFIG = {
    # Example committee configs; extend to 10 committees
    "finance_audit": {
        "template_id": "finance_audit_template",
        "frequency": ["quarterly", "annual"],
    },
    "risk_committee": {
        "template_id": "risk_committee_template",
        "frequency": ["quarterly", "halfyearly", "annual"],
    },
    # ...
}
