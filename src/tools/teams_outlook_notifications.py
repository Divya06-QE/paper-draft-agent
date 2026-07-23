import requests
from typing import Optional
from ..config import TEAMS_WEBHOOK_URL, OUTLOOK_SENDER_ADDRESS


def send_teams_notification(message: str, link: Optional[str] = None):
    payload = {
        "text": message if not link else f"{message}\n\nDraft link: {link}"
    }
    requests.post(TEAMS_WEBHOOK_URL, json=payload)


def send_outlook_notification(recipient: str, subject: str, body: str):
    """
    Placeholder: in production, use Graph API or SMTP with service account.
    """
    print(f"[OUTLOOK] To: {recipient} | Subject: {subject}\n{body}")
