# utils/prompt_builder.py

from agents.knowledge_agent import get_knowledge


def build_prompt(
        requirement,
        purpose,
        extra_instructions=""
):

    knowledge = get_knowledge(requirement)

    prompt = f"""
Purpose:
{purpose}

Requirement:
{requirement}

Knowledge:
{knowledge}

Rules:
- Plain text only
- No markdown
- No # symbols
- No * symbols
- No bullet points
- No tables
- No code fences
- No --- separators

{extra_instructions}
"""

    return prompt