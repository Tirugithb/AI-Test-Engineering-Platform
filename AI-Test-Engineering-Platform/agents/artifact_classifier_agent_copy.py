# agents/artifact_classifier_agent.py

def classify_artifact(requirement):
    print("================================")
    print("CLASSIFIER INPUT")
    print(requirement)
    print("================================")

    requirement = requirement.lower()

    # Only classify the USER REQUEST section
    if "user request:" in requirement:
        requirement = requirement.split(
            "=================================="
        )[0]

    print(requirement)

    print("================================")
    print(requirement)
    print("================================")

    # ==========================
    # DOCUMENT AGENT
    # ==========================

    # Extract Requirements
    if (
            "extract" in requirement
            and (
            "requirement" in requirement
            or "requirements" in requirement
    )
    ):
        return "document_requirements"

    # Identify Risks
    elif (
            "risk" in requirement
    ):
        return "document_risks"

    # Action Items
    elif (
            "action item" in requirement
    ):
        return "document_actions"

    # Summary
    elif (
            "summarize" in requirement
            and "document" in requirement
    ):
        return "document_summary"

    # Analysis
    elif (
            "analyze" in requirement
            and "document" in requirement
    ):
        return "document_analysis"

    if any(keyword in requirement for keyword in [
        "generate test case",
        "generate test cases",
        "test case",
        "test cases"
    ]) and "api" not in requirement:
        return "test_cases"

    elif "test plan" in requirement:
        return "test_plan"

    elif "test strategy" in requirement:
        return "test_strategy"

    elif "sql query" in requirement:
        return "sql_query"

    elif "stored procedure" in requirement:
        return "stored_procedure"

    # elif any(keyword in requirement for keyword in [
    #     "python code",
    #     "generate python",
    #     "python script",
    #     "python program",
    #     "write python",
    #     "python"
    # ]):
    #     return "python_code"

    elif any(keyword in requirement for keyword in [
        "rtm",
        "requirements traceability matrix",
        "requirement traceability matrix",
        "traceability matrix"
    ]):
        return "rtm"

    elif any(keyword in requirement for keyword in [
        "generate sql function",
        "create sql function",
        "sql function"
    ]):
        return "function"

    elif any(keyword in requirement for keyword in [
        "generate view",
        "create view",
        "sql view"
    ]):
        return "view"

    elif any(keyword in requirement for keyword in [
        "generate trigger",
        "create trigger",
        "sql trigger"
    ]):
        return "trigger"

    elif any(keyword in requirement for keyword in [
        "generate pom",
        "create pom",
        "page object model",
        "pom"
    ]):

        return "pom"

    elif "ci/cd" in requirement:
        return "cicd"

    elif any(keyword in requirement for keyword in [
        "jenkins",
        "github actions",
        "azure devops",
        "pipeline",
        "ci/cd",
        "cicd"
    ]):
        return "cicd"

    elif any(keyword in requirement for keyword in [
        "appium",
        "selenium",
        "playwright",
        "automation",
        "python automation"
    ]):
        return "automation_script"

    # ==========================
    # REQUIREMENT AGENT
    # ==========================

    elif any(keyword in requirement for keyword in [
        "generate brd",
        "business requirements document",
        "brd"
    ]):
        return "brd"

    elif any(keyword in requirement for keyword in [
        "generate frs",
        "functional requirements specification",
        "frs"
    ]):
        return "frs"

    elif any(keyword in requirement for keyword in [
        "generate user stories",
        "generate user story",
        "user stories",
        "user story"
    ]):
        return "user_story"

    elif any(keyword in requirement for keyword in [
        "generate acceptance criteria",
        "acceptance criteria"
    ]):
        return "acceptance_criteria"

    elif any(keyword in requirement for keyword in [
        "generate use case",
        "generate use cases",
        "use case",
        "use cases"
    ]):
        return "use_case"

    elif any(keyword in requirement for keyword in [
        "generate epic",
        "generate epics",
        "epic",
        "epics"
    ]):
        return "epic"

    elif any(keyword in requirement for keyword in [

        "generate functional requirements",
        "functional requirements"

    ]) and "non functional" not in requirement and "non-functional" not in requirement:

        return "functional_requirements"

    elif any(keyword in requirement for keyword in [
        "generate non functional requirements",
        "generate non-functional requirements",
        "non functional requirements",
        "non-functional requirements"
    ]):
        return "non_functional_requirements"

    # ==========================
    # API AGENT
    # ==========================

    elif any(keyword in requirement for keyword in [
        "generate api test cases",
        "api test cases",
        "api testcase",
        "api test case"
    ]):
        return "api_test_cases"

    elif any(keyword in requirement for keyword in [
        "generate postman collection",
        "postman collection"
    ]):
        return "postman_collection"

    elif any(keyword in requirement for keyword in [
        "generate rest assured",
        "generate restassured",
        "rest assured framework",
        "rest assured",
        "restassured"
    ]):
        return "rest_assured"

    elif any(keyword in requirement for keyword in [
        "generate swagger",
        "swagger specification",
        "swagger"
    ]):
        return "swagger"

    elif any(keyword in requirement for keyword in [
        "generate openapi",
        "openapi specification",
        "openapi"
    ]):
        return "openapi"

    elif any(keyword in requirement for keyword in [
        "python",
        "java",
        "spring boot",
        "rest api",
        "flask",
        "django",
        "fastapi",
        "c#",
        "javascript",
        "node",
        "react",
        "angular",
        "html",
        "css"
    ]):
        return "code_generation"

    elif "defect report" in requirement:
        return "defect_report"

    elif "test summary report" in requirement:
        return "test_summary_report"

    elif "release report" in requirement:
        return "release_report"

    elif "test metrics" in requirement:
        return "test_metrics"

    return "full_suite"

