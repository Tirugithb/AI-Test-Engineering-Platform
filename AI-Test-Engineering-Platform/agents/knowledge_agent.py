# agents/knowledge_agent.py

from utils.knowledge_reader import read_knowledge
from agents.knowledge_classifier_agent import classify_requirement
from agents.technology_classifier_agent import (
    classify_technology
)
from agents.domain_classifier_agent import (
    classify_domain
)


def get_knowledge(requirement):

    categories = classify_requirement(
        requirement
    )

    technology = classify_technology(
        requirement
    )

    domain = classify_domain(
        requirement
    )

    knowledge = ""

    # Functional Knowledge
    if "functional" in categories:
        knowledge += read_knowledge(
            "functional_testing.txt"
        )

    # UI Knowledge
    if "ui" in categories:
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "ui_testing.txt"
        )

    # API Knowledge
    if "api" in categories:
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "api_testing.txt"
        )

    # Security Knowledge
    if "security" in categories:
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "security_testing.txt"
        )

    # Automation Knowledge
    if "automation" in categories:
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "automation_best_practices.txt"
        )

    # Domain Knowledge

    if domain == "healthcare":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "healthcare_testing.txt"
        )

    elif domain == "insurance":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "insurance_testing.txt"
        )

    elif domain == "ecommerce":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "ecommerce_testing.txt"
        )

    elif domain == "etl":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "etl_testing.txt"
        )

    elif domain == "salesforce":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "salesforce_testing.txt"
        )

    elif domain == "aws":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "aws_testing.txt"
        )

    if technology == "appium":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "appium_testing.txt"
        )

    elif technology == "selenium":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "selenium_testing.txt"
        )

    elif technology == "playwright":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "playwright_testing.txt"
        )

    elif technology == "sql":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "sql_testing.txt"
        )

    elif technology == "python":
        knowledge += "\n\n"
        knowledge += read_knowledge(
            "python_testing.txt"
        )

    return knowledge