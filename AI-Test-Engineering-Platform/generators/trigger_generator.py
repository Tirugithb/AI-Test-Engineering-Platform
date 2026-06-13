# generators/trigger_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_trigger(requirement):
    """
    Generate SQL Trigger.
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate SQL Trigger.

Rules:
1. Return only SQL code.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality SQL.
6. Include CREATE TRIGGER statement.
7. Use meaningful trigger names.
8. Include business validation logic.
9. Include audit logging if applicable.
10. Include proper error handling.
11. Use best SQL practices.
12. Generate complete executable SQL.
13. Avoid placeholder values.
14. Use realistic table and column names.
15. Support INSERT, UPDATE or DELETE events based on requirement.
"""
    )

    return generate_ai_response(prompt)