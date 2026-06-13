# agents/technology_classifier_agent.py

def classify_technology(requirement):

    requirement = requirement.lower()

    if "appium" in requirement:
        return "appium"

    elif "selenium" in requirement:
        return "selenium"

    elif "playwright" in requirement:
        return "playwright"

    elif "sql" in requirement:
        return "sql"

    elif "aws" in requirement:
        return "aws"

    elif "salesforce" in requirement:
        return "salesforce"

    elif "api" in requirement:
        return "api"

    elif "python" in requirement:
        return "python"

    return "general"