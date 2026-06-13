# generators/github_actions_generator.py

from llm.openai_client import generate_ai_response


def generate_github_actions(requirement):

    prompt = f"""
Generate GitHub Actions Workflow.

Requirement:
{requirement}

Rules:
1. Return only YAML code.
2. No explanations.
3. No markdown.
4. Generate GitHub Actions workflow.
5. Include Checkout step.
6. Include Dependency Installation.
7. Include Test Execution.
8. Include Report Publishing.
9. Include Artifact Upload.
10. Production-ready workflow.
"""

    return generate_ai_response(prompt)