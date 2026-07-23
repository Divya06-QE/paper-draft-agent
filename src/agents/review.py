from typing import TypedDict
from ..models import get_llm


class ReviewState(TypedDict):
    draft_text: str
    reviewed_text: str


def review_node(state: ReviewState) -> ReviewState:
    llm = get_llm()
    prompt = f"""
You are a senior governance reviewer.

Review the following draft paper for:
- clarity
- consistency
- missing sections
- tone appropriate for board/committee

Return an improved version, preserving structure.

Draft:
{state['draft_text']}
"""
    response = llm.invoke(prompt)
    state["reviewed_text"] = response.content
    return state
