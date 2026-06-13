from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_sql(requirement):

    prompt = build_advanced_prompt(
        requirement,
        "SQL Queries",
        """
Generate SQL only.

Rules:
1. Return SQL code only.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality SQL.
6. Generate validation queries.
7. Include positive, negative and data validation queries.
8. Include joins when applicable.
9. Include aggregation queries when applicable.
"""
    )

    return generate_ai_response(prompt)