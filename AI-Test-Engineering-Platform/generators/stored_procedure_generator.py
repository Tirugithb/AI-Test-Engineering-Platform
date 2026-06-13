# generators/stored_procedure_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_stored_procedure(requirement):
    """
    Generate SQL Stored Procedure.
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate SQL Stored Procedure.

Rules:
1. Return only SQL code.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality SQL.
6. Include CREATE PROCEDURE statement.
7. Include input parameters if applicable.
8. Include validation logic.
9. Include error handling.
10. Use best SQL practices.
"""
    )

    return generate_ai_response(prompt)