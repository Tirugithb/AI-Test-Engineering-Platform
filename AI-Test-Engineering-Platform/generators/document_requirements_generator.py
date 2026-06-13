from llm.openai_client import generate_ai_response


def generate_document_requirements(requirement):

    prompt = f"""
You are an expert Business Analyst.

Your ONLY task is to extract requirements from the uploaded document.

IMPORTANT:

DO NOT:
- Summarize the document
- Generate Executive Summary
- Generate Key Topics
- Generate Important Findings
- Generate Risks
- Generate Recommendations
- Generate Action Items

ONLY extract requirements.

Return exactly in this format:

# Functional Requirements

- ...

# Business Requirements

- ...

# Technical Requirements

- ...

# Assumptions

- ...

# Constraints

- ...

==============================

Uploaded Document:

{requirement}

==============================
"""

    return generate_ai_response(prompt)