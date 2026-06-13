from llm.openai_client import generate_ai_response


def generate_document_actions(requirement):

    prompt = f"""
Analyze the uploaded document.

Generate:

1. Action Items
2. Recommendations
3. Next Steps
4. Improvements

Return only actionable items.

Document:

{requirement}
"""

    return generate_ai_response(prompt)