from llm.openai_client import generate_ai_response


def generate_document_risks(requirement):

    prompt = f"""
Analyze the uploaded document.

Identify:

1. Risks
2. Gaps
3. Missing Information
4. Potential Issues
5. Improvement Areas

Return only the risks and observations.

Document:

{requirement}
"""

    return generate_ai_response(prompt)