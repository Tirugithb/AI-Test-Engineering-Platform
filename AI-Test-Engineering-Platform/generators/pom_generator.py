# generators/pom_generator.py

from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def generate_pom(requirement):
    """
    Generate Page Object Model (POM)
    for Appium, Selenium or Playwright.
    """

    prompt = build_advanced_prompt(
        requirement,
        """
Generate Page Object Model (POM).

Rules:
1. Return only code.
2. No explanations.
3. No markdown.
4. No code fences.
5. Generate production-quality code.
6. Follow Page Object Model design pattern.
7. Include locators.
8. Include actions/methods.
9. Include assertions when applicable.
10. Include reusable functions.
11. Use best automation practices.
12. Generate complete executable code.
13. Use Appium, Selenium or Playwright based on requirement.
14. Include imports.
15. Include class definition.
16. Use meaningful locator names.
17. Use explicit waits whenever applicable.
18. Avoid placeholder values.
"""
    )

    return generate_ai_response(prompt)