from typing import TypedDict
from ..config import COMMITTEE_CONFIG


class RouterState(TypedDict):
    committee_id: str
    period: str
    year: int
    user_upn: str
    committee_template_id: str


def committee_router_node(state: RouterState) -> RouterState:
    committee_id = state["committee_id"]
    period = state["period"]

    config = COMMITTEE_CONFIG.get(committee_id)
    if not config:
        raise ValueError(f"Unknown committee: {committee_id}")

    if period not in config["frequency"]:
        raise ValueError(f"Period {period} not supported for committee {committee_id}")

    state["committee_template_id"] = config["template_id"]
    return state
