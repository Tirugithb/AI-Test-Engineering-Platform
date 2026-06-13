from llm.openai_client import generate_ai_response


def generate_document_summary(requirement):

    prompt = f"""
You are an expert Document Analysis AI.

Your task is ONLY to summarize the uploaded document.

STRICT RULES:

- Do NOT generate Test Cases.
- Do NOT generate Test Plan.
- Do NOT generate Test Strategy.
- Do NOT generate SQL.
- Do NOT generate Code.
- Do NOT create examples.
- Do NOT invent information.

Read the uploaded document carefully and provide:

1. Executive Summary
2. Key Topics
3. Important Findings

==============================

{requirement}

==============================

Return only the summary.
"""

    return generate_ai_response(prompt)