# generators/test_summary_report_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_test_summary_report(requirement):

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Test Summary Report.

Rules:
1. Plain text only.
2. No markdown.
3. Include Project Name.
4. Include Scope.
5. Include Total Test Cases.
6. Include Passed.
7. Include Failed.
8. Include Blocked.
9. Include Defects Summary.
10. Include Risks.
11. Include Recommendations.
12. Enterprise-quality report.
13. Do not fabricate metrics.
14. Use TBD if actual execution data is unavailable.
15. Do not assume execution results.
16. Clearly indicate when metrics are not provided.
17. Use actual values only if they are explicitly supplied in the requirement.
"""
    )

    return generate_ai_response(prompt)