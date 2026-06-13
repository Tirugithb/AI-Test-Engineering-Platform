# generators/azure_devops_generator.py

from llm.openai_client import generate_ai_response


def generate_azure_pipeline(requirement):

    prompt = f"""
Generate Azure DevOps Pipeline.

Requirement:
{requirement}

Rules:
1. Return only YAML code.
2. No explanations.
3. No markdown.
4. Generate Azure DevOps pipeline.
5. Include Checkout stage.
6. Include Dependency Installation.
7. Include Test Execution.
8. Include Report Publishing.
9. Include Artifact Publishing.
10. Production-ready pipeline.
"""

    return generate_ai_response(prompt)