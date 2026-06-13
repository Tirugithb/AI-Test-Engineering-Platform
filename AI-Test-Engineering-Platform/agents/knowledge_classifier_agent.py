# agents/knowledge_classifier_agent.py

def classify_requirement(requirement):

    requirement = requirement.lower()

    categories = ["functional"]

    if any(word in requirement for word in [
        "login",
        "password",
        "authentication",
        "authorization",
        "security"
    ]):
        categories.append("security")

    if any(word in requirement for word in [
        "api",
        "rest",
        "service",
        "endpoint"
    ]):
        categories.append("api")

    if any(word in requirement for word in [
        "ui",
        "screen",
        "page",
        "form",
        "button"
    ]):
        categories.append("ui")

    if any(word in requirement for word in [
        "selenium",
        "appium",
        "playwright",
        "automation"
    ]):
        categories.append("automation")

    return categories