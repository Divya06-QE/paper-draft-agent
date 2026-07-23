from typing import TypedDict, Dict, Any
from ..models import get_llm
from ..tools.templates import render_template


class DraftState(TypedDict):
    committee_id: str
    period: str
    year: int
    user_upn: str
    committee_template_id: str
    aggregated_context: Dict[str, Any]
    draft_text: str


def drafting_node(state: DraftState) -> DraftState:
    llm = get_llm()

    prompt = f"""
You are an expert governance and finance paper drafter.

Committee: {state['committee_id']}
Period: {state['period']} {state['year']}

Use the aggregated context below to pre-fill the committee-specific template.
Focus on clarity, compliance, and concise summarisation.

Aggregated context:
{state['aggregated_context']}
"""

    response = llm.invoke(prompt)
    # Option 1: let the model produce structured fields, then render template.
    # For simplicity, we treat response as a free-form summary and inject into template.
    context = {
        "committee_name": state["committee_id"],
        "period": state["period"],
        "year": state["year"],
        "meeting_range": "Meetings in the period",
        "agenda_summary": state["aggregated_context"].get("agenda_summary", ""),
        "key_points": state["aggregated_context"].get("key_points", ""),
        "action_items": state["aggregated_context"].get("action_items", ""),
        "next_steps": state["aggregated_context"].get("next_steps", ""),
        "financial_highlights": state["aggregated_context"].get("financial_highlights", ""),
        "attachments": state["aggregated_context"].get("attachments", ""),
        "executive_summary": response.content,
        "key_risks": "",
        "mitigation_actions": "",
        "decisions": "",
        "follow_up_items": "",
    }

    draft_text = render_template(state["committee_template_id"], context)
    state["draft_text"] = draft_text
    return state
