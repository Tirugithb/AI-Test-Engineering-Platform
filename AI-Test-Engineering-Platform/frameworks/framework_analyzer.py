# frameworks/framework_analyzer.py

def analyze_framework(requirement):

    requirement = requirement.lower()

    if "appium" in requirement:
        return "APPIUM"

    elif "playwright" in requirement:
        return "PLAYWRIGHT"

    elif "selenium" in requirement:
        return "SELENIUM"

    else:
        return "SELENIUM"