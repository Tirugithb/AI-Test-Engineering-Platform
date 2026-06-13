# analyzers/requirement_analyzer.py

def analyze_requirement(requirement):

    requirement = requirement.lower()

    if "login" in requirement:
        return "LOGIN"

    elif "registration" in requirement:
        return "REGISTRATION"

    elif "register" in requirement:
        return "REGISTRATION"

    elif "forgot password" in requirement:
        return "FORGOT_PASSWORD"

    elif "search" in requirement:
        return "SEARCH"

    else:
        return "GENERIC"