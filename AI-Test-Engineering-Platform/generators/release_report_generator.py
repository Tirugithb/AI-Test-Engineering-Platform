# generators/release_report_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_release_report(requirement):

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Release Report.

Rules:
1. Plain text only.
2. No markdown.
3. Include Release Version.
4. Include Features Delivered.
5. Include Test Execution Summary.
6. Include Defects Summary.
7. Include Risks.
8. Include Go/No-Go Recommendation.
9. Enterprise-quality release report.
10. Do not fabricate metrics.
11. Use TBD if actual execution data is unavailable.
12. Do not assume execution results.
13. Clearly indicate when metrics are not provided.
14. Use actual values only if they are explicitly supplied in the requirement.
15. Use TBD for pass/fail counts, defect counts, coverage percentages, and execution metrics when no data is available.
"""
    )

    return generate_ai_response(prompt)
