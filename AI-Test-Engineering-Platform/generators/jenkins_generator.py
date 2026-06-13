# generators/jenkins_generator.py

from llm.openai_client import generate_ai_response


def generate_jenkins_pipeline(requirement):

    prompt = f"""
Generate Jenkins Pipeline.

Requirement:
{requirement}

Rules:
1. Return only Jenkinsfile code.
2. No explanations.
3. No markdown.
4. Use declarative pipeline.
5. Include Checkout.
6. Include Dependency Installation.
7. Include Test Execution.
8. Include Report Publishing.
9. Include Post Actions.
10. Production-ready pipeline.
"""

    return generate_ai_response(prompt)