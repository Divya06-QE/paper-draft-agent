from typing import TypedDict
from ..tools.sharepoint_client import SharePointClient
from ..tools.teams_outlook_notifications import send_teams_notification, send_outlook_notification


class NotificationState(TypedDict):
    committee_id: str
    period: str
    year: int
    user_upn: str
    reviewed_text: str
    draft_url: str


def notification_node(state: NotificationState) -> NotificationState:
    sp = SharePointClient()

    file_name = f"{state['committee_id']}_{state['period']}_{state['year']}_draft.docx"
    draft_url = sp.save_draft(
        user_upn=state["user_upn"],
        committee_id=state["committee_id"],
        file_name=file_name,
        content=state["reviewed_text"],
    )
    state["draft_url"] = draft_url

    message = (
        f"Draft paper generated for committee '{state['committee_id']}' "
        f"for {state['period']} {state['year']}."
    )
    send_teams_notification(message, link=draft_url)

    subject = f"Draft paper ready – {state['committee_id']} ({state['period']} {state['year']})"
    body = f"The draft paper has been generated and stored at:\n{draft_url}"
    send_outlook_notification(recipient=state["user_upn"], subject=subject, body=body)

    return state
