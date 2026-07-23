from typing import TypedDict
from langgraph.graph import StateGraph, END

from .agents.committee_router import committee_router_node
from .agents.data_ingestion import data_ingestion_node
from .agents.drafting import drafting_node
from .agents.review import review_node
from .agents.notification import notification_node


class PaperState(TypedDict):
    committee_id: str
    period: str
    year: int
    user_upn: str
    committee_template_id: str
    meetings: list
    previous_papers: list
    aggregated_context: dict
    draft_text: str
    reviewed_text: str
    draft_url: str


def build_graph() -> StateGraph:
    graph = StateGraph(PaperState)

    graph.add_node("router", committee_router_node)
    graph.add_node("data_ingestion", data_ingestion_node)
    graph.add_node("drafting", drafting_node)
    graph.add_node("review", review_node)
    graph.add_node("notification", notification_node)

    graph.set_entry_point("router")
    graph.add_edge("router", "data_ingestion")
    graph.add_edge("data_ingestion", "drafting")
    graph.add_edge("drafting", "review")
    graph.add_edge("review", "notification")
    graph.add_edge("notification", END)

    return graph
