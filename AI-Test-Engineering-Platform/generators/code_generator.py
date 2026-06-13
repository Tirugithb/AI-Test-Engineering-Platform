from llm.openai_client import generate_ai_response


def generate_code(requirement):

    prompt = f"""
You are an expert software engineer.

Generate complete production-ready code.

Requirement:

{requirement}

Return only the code with brief explanation.
"""

    return generate_ai_response(prompt)