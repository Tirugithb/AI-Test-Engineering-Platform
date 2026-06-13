# generators/rtm_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_rtm(requirement):
    """
    Generate Requirements Traceability Matrix (RTM)
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Requirements Traceability Matrix (RTM).

Rules:
1. Return plain text only.
2. No markdown.
3. No code fences.
4. Generate enterprise-quality RTM.
5. Include Requirement IDs.
6. Include Requirement Description.
7. Include Test Case IDs.
8. Include Test Case Description.
9. Include Coverage Status.
10. Include Priority.
11. Include Test Type.
12. Include Traceability Mapping.
13. Generate complete RTM.
14. Use realistic requirement IDs.
15. Use realistic test case IDs.

Format:

Requirement ID
Requirement Description
Test Case ID
Test Case Description
Priority
Test Type
Coverage Status
Remarks
"""
    )

    return generate_ai_response(prompt)