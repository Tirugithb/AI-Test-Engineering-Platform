from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_test_plan(requirement):
    """
    Generate AI-powered Test Plan based on the provided requirement.
    """

    prompt = build_advanced_prompt(
        requirement,
        "Software Test Plan",
        """
Include:

Objectives

Scope

Test Types

Entry Criteria

Exit Criteria

Risks

Deliverables

Assumptions

Dependencies

Use professional QA documentation format.

Suitable for direct export to TXT.
"""
    )

    return generate_ai_response(prompt)