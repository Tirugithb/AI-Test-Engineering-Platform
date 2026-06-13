# generators/automation_script_generator.py

from analyzers.requirement_analyzer import analyze_requirement
from frameworks.framework_analyzer import analyze_framework


def generate_automation_script(requirement):

    flow_type = analyze_requirement(requirement)
    framework = analyze_framework(requirement)

    # LOGIN FLOW
    if flow_type == "LOGIN":

        if framework == "APPIUM":
            return """
# Appium Login Automation Script

from appium import webdriver

print("Executing Appium Login Automation")

# Add Appium login automation here
"""

        elif framework == "PLAYWRIGHT":
            return """
# Playwright Login Automation Script

from playwright.sync_api import sync_playwright

print("Executing Playwright Login Automation")

# Add Playwright login automation here
"""

        else:
            return """
# Selenium Login Automation Script

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com/login")

print("Executing Selenium Login Automation")

driver.quit()
"""

    # REGISTRATION FLOW
    elif flow_type == "REGISTRATION":

        if framework == "APPIUM":
            return """
# Appium Registration Automation Script

from appium import webdriver

print("Executing Appium Registration Automation")
"""

        elif framework == "PLAYWRIGHT":
            return """
# Playwright Registration Automation Script

from playwright.sync_api import sync_playwright

print("Executing Playwright Registration Automation")
"""

        else:
            return """
# Selenium Registration Automation Script

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com/register")

print("Executing Selenium Registration Automation")

driver.quit()
"""

    # FORGOT PASSWORD FLOW
    elif flow_type == "FORGOT_PASSWORD":

        if framework == "APPIUM":
            return """
# Appium Forgot Password Automation Script

from appium import webdriver

print("Executing Appium Forgot Password Automation")
"""

        elif framework == "PLAYWRIGHT":
            return """
# Playwright Forgot Password Automation Script

from playwright.sync_api import sync_playwright

print("Executing Playwright Forgot Password Automation")
"""

        else:
            return """
# Selenium Forgot Password Automation Script

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com/forgot-password")

print("Executing Selenium Forgot Password Automation")

driver.quit()
"""

    # SEARCH FLOW
    elif flow_type == "SEARCH":

        if framework == "APPIUM":
            return """
# Appium Search Automation Script

from appium import webdriver

print("Executing Appium Search Automation")
"""

        elif framework == "PLAYWRIGHT":
            return """
# Playwright Search Automation Script

from playwright.sync_api import sync_playwright

print("Executing Playwright Search Automation")
"""

        else:
            return """
# Selenium Search Automation Script

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com/search")

print("Executing Selenium Search Automation")

driver.quit()
"""

    # GENERIC FLOW
    else:

        return """
# Generic Selenium Automation Script

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")

print("Executing Generic Automation")

driver.quit()
"""