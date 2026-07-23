from typing import Dict, Any


TEMPLATES: Dict[str, str] = {
    "finance_audit_template": """
# Finance & Audit Committee Report – {period} {year}

## Meeting Summary
- Committee: {committee_name}
- Period: {period}
- Meetings covered: {meeting_range}

## Agenda Overview
{agenda_summary}

## Key Discussion Points
{key_points}

## Action Items
{action_items}

## Next Steps
{next_steps}

## Financial Highlights
{financial_highlights}

## Attachments / References
{attachments}
""",
    "risk_committee_template": """
# Risk Committee Report – {period} {year}

## Executive Summary
{executive_summary}

## Key Risks Discussed
{key_risks}

## Mitigation Actions
{mitigation_actions}

## Decisions & Resolutions
{decisions}

## Follow-up Items
{follow_up_items}
""",
    # Add templates for remaining committees
}


def render_template(template_id: str, context: Dict[str, Any]) -> str:
    template = TEMPLATES.get(template_id, "")
    return template.format(**context)
