# utils/advanced_prompt_builder.py

from agents.domain_classifier_agent import (
    classify_domain
)

from agents.technology_classifier_agent import (
    classify_technology
)

from agents.knowledge_agent import (
    get_knowledge
)


def build_advanced_prompt(
        requirement,
        artifact_type,
        additional_instructions=""
):

    domain = classify_domain(
        requirement
    )

    technology = classify_technology(
        requirement
    )

    knowledge = get_knowledge(
        requirement
    )

    prompt = f"""
Generate {artifact_type}.

Requirement:
{requirement}

Domain:
{domain}

Technology:
{technology}

Knowledge:
{knowledge}

Rules:
- Plain text only
- No markdown
- No # symbols
- No * symbols
- No tables
- No code fences
- Professional QA format
- Use domain knowledge
- Use technology knowledge
- Avoid generic content
- Generate enterprise-level output

{additional_instructions}
"""

    return prompt