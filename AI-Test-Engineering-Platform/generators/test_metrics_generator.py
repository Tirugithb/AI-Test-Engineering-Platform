# generators/test_metrics_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_test_metrics(requirement):

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Test Metrics Report.

Rules:
1. Plain text only.
2. No markdown.
3. Include Test Execution Metrics.
4. Include Pass Percentage.
5. Include Fail Percentage.
6. Include Defect Density.
7. Include Defect Leakage.
8. Include Automation Coverage.
9. Include Recommendations.
10. Enterprise-quality metrics report.
11. Do not fabricate metrics.
12. Use TBD if actual execution data is unavailable.
13. Do not assume execution results.
14. Clearly indicate when metrics are not provided.
15. Use actual values only if they are explicitly supplied in the requirement.
16. Use TBD for pass rate, fail rate, defect density, defect leakage, automation coverage, and execution counts when no data is available.
"""
    )

    return generate_ai_response(prompt)