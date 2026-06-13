# generators/view_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_view(requirement):
    """
    Generate SQL View.
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate SQL View.

Rules:
1. Return only SQL code.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality SQL.
6. Include CREATE VIEW statement.
7. Use meaningful view names.
8. Include proper column aliases when needed.
9. Apply business rules and filters.
10. Use best SQL practices.
11. Generate complete executable SQL.
12. Avoid placeholder values.
13. Use realistic table and column names.
"""
    )

    return generate_ai_response(prompt)