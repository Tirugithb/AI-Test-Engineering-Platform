from llm.openai_client import generate_ai_response


def generate_document_analysis(requirement):

    prompt = f"""
You are an intelligent document analysis assistant.

First identify the document type.

Then analyze it appropriately.

Provide:

1. Document Type
2. Executive Summary
3. Key Topics
4. Important Findings
5. Risks / Issues (if applicable)
6. Recommendations
7. Action Items
8. Overall Conclusion

Do NOT generate test cases unless the uploaded document itself asks for test cases.

Document:

{requirement}
"""

    return generate_ai_response(prompt)