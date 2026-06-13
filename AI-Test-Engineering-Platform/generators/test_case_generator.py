# generators/test_case_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_test_case(requirement):
    """
    Generate AI-powered test cases based on the provided requirement.
    """

    prompt = build_advanced_prompt(
        requirement,
        "Enterprise Test Cases",
        """
Include:

TC ID
Module
Test Case Description
Preconditions
Test Steps
Expected Result
Priority
Test Type

Generate:
Positive Testing
Negative Testing
Boundary Testing
Integration Testing
Regression Testing
Security Testing
Performance Testing

Generate at least 10 comprehensive test cases.
"""
    )

    return generate_ai_response(prompt)