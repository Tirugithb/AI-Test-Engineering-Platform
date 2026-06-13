# generators/function_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_function(requirement):
    """
    Generate SQL Function.
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate SQL Function.

Rules:
1. Return only SQL code.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality SQL.
6. Include CREATE FUNCTION statement.
7. Include input parameters if applicable.
8. Include validation logic.
9. Include business rules.
10. Include proper RETURN statement.
11. Use best SQL practices.
12. Function should be executable.
13. Avoid placeholder values.
14. Generate complete SQL function.
"""
    )

    return generate_ai_response(prompt)