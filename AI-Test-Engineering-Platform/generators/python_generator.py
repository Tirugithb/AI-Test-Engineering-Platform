from llm.openai_client import generate_ai_response

def generate_python(requirement):

    prompt = f"""
You are an expert Python developer.

Generate complete, well-commented Python code for the following requirement.

Requirement:
{requirement}

Return only the Python code.
"""

    return generate_ai_response(prompt)