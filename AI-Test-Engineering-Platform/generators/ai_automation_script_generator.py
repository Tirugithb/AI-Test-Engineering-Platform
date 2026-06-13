from llm.openai_client import generate_ai_response
from utils.advanced_prompt_builder import (
    build_advanced_prompt
)


def clean_code(response):

    response = response.replace("```python", "")
    response = response.replace("```", "")

    return response.strip()


def generate_ai_automation_script(requirement):
    """
    Generate AI-powered automation script.
    """

    prompt = build_advanced_prompt(
        requirement,
        "Automation Script",
        """
Generate ONLY executable code.

Rules:
1. Return only code.
2. No explanations.
3. No markdown.
4. No code fences.
5. No notes.
6. Start directly with import statements.
7. Include imports, setup, test steps, assertions and cleanup.
8. Use Selenium, Appium, Playwright, API, SQL or Python based on the requirement.
9. Follow automation best practices.
10. Use explicit waits whenever applicable.
11. Use assertions.
12. Use exception handling.
13. Return executable production-quality code only.
14. Do not generate placeholder variables.
15. Do not generate undefined objects.
16. If schema validation is used, generate the complete schema.
17. Generated code must run without unresolved references.
18. Use reusable functions whenever applicable.
19. Use logging whenever applicable.
20. Generate maintainable framework-ready code.
"""
    )

    script = generate_ai_response(prompt)

    return clean_code(script)