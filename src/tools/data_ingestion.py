from typing import TypedDict, List, Dict, Any
from ..tools.sharepoint_client import SharePointClient
from ..tools.dataverse_client import DataverseClient


class DataState(TypedDict):
    committee_id: str
    period: str
    year: int
    user_upn: str
    committee_template_id: str
    meetings: List[Dict[str, Any]]
    previous_papers: List[Dict[str, Any]]
    aggregated_context: Dict[str, Any]


def data_ingestion_node(state: DataState) -> DataState:
    committee_id = state["committee_id"]
    period = state["period"]

    sp = SharePointClient()
    dv = DataverseClient()

    meetings = dv.get_meeting_records(committee_id, period)
    previous_papers = sp.get_previous_papers(committee_id)

    # Simple aggregation; you can enrich this heavily
    aggregated_context = {
        "agenda_summary": "Summary of agendas from Dataverse records.",
        "key_points": "Key points extracted from meeting notes.",
        "action_items": "Action items derived from Dataverse tasks.",
        "next_steps": "Next steps agreed in meetings.",
        "financial_highlights": "Financial highlights from previous papers.",
        "attachments": "Links to relevant documents.",
    }

    state["meetings"] = meetings
    state["previous_papers"] = previous_papers
    state["aggregated_context"] = aggregated_context
    return state
