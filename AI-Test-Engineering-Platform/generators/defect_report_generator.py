# generators/defect_report_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_defect_report(requirement):

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Defect Report.

Rules:
1. Plain text only.
2. No markdown.
3. Generate enterprise-quality defect report.
4. Include Defect ID.
5. Include Summary.
6. Include Description.
7. Include Severity.
8. Include Priority.
9. Include Steps to Reproduce.
10. Include Expected Result.
11. Include Actual Result.
12. Include Status.
"""
    )

    return generate_ai_response(prompt)