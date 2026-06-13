from utils.advanced_prompt_builder import (
    build_advanced_prompt
)

prompt = build_advanced_prompt(
    "Generate SQL validation for Insurance Claims",
    "Enterprise Test Cases",
    """
Include:
TC ID
Module
Description
Preconditions
Steps
Expected Result
Priority
Test Type
"""
)

print(prompt)