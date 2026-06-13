# agents/artifact_classifier_agent.py

def match(requirement, keywords):
    """
    Returns True if any keyword exists.
    """

    return any(
        keyword in requirement
        for keyword in keywords
    )
RULES = [

    (
        "devops",
        [
            "devops",
            "docker",
            "dockerfile",
            "docker compose",
            "kubernetes",
            "helm",
            "terraform",
            "ansible",
            "jenkins",
            "github actions",
            "gitlab ci",
            "azure devops",
            "aws codepipeline",
            "aws codebuild",
            "aws codedeploy",
            "argocd",
            "fluxcd",
            "pipeline",
            "ci/cd",
            "cicd",
            "deployment",
            "infrastructure as code"

        ]
    ),

    (
        "api",
        [

            "api",
            "rest api",
            "graphql",
            "soap",
            "swagger",
            "openapi",
            "postman",
            "postman collection",
            "rest assured",
            "api test cases",
            "api testcase",
            "api automation",
            "json schema",
            "xml schema",
            "oauth",
            "jwt",
            "bearer token",
            "crud api",
            "endpoint"

        ]
    ),

    (
        "requirement",
        [

            "brd",
            "business requirements document",
            "frs",
            "functional requirements specification",
            "user story",
            "user stories",
            "epic",
            "epics",
            "acceptance criteria",
            "use case",
            "use cases",
            "functional requirements",
            "non functional requirements",
            "non-functional requirements",
            "business requirements",
            "stakeholder analysis",
            "gap analysis",
            "rtm",
            "requirements traceability matrix",
            "business rules",
            "process flow"

        ]
    ),

    (
        "database_sql",
        [

            # General
            "sql",
            "query",
            "database",
            "table",
            "schema",

            # DDL
            "ddl",
            "create table",
            "alter table",
            "drop table",
            "truncate table",
            "rename table",
            "create database",
            "create schema",

            # DML
            "insert",
            "update",
            "delete",
            "merge",
            "upsert",

            # DQL
            "select",
            "where",
            "group by",
            "having",
            "order by",
            "distinct",

            # DCL
            "grant",
            "revoke",

            # TCL
            "commit",
            "rollback",
            "savepoint",
            "transaction",

            # Joins
            "join",
            "inner join",
            "left join",
            "right join",
            "full join",
            "cross join",
            "self join",

            # Window Functions
            "lead",
            "lag",
            "lead lag",
            "row number",
            "rank",
            "dense rank",
            "ntile",
            "first value",
            "last value",

            # CTE
            "cte",
            "recursive cte",
            "common table expression",

            # Pivot
            "pivot",
            "unpivot",

            # Subqueries
            "subquery",
            "correlated subquery",
            "exists",
            "not exists",

            # Duplicates
            "duplicate",
            "duplicates",
            "find duplicate",
            "remove duplicate",

            # Hierarchy
            "hierarchy",
            "employee hierarchy",
            "manager",
            "sub-manager",
            "organization chart",

            # SCD
            "scd",
            "slowly changing dimension",
            "scd type 1",
            "scd type 2",
            "scd type 3",
            "scd type 4",
            "scd type 6",

            # Objects
            "stored procedure",
            "procedure",
            "function",
            "trigger",
            "view",
            "sequence",

            # Database Design
            "er diagram",
            "entity relationship",
            "database schema",
            "table design",
            "data dictionary",
            "sample data",
            "normalization",
            "denormalization",
            "partition",
            "index",
            "optimization",
            "execution plan",

            # Interview Problems
            "second highest salary",
            "nth highest salary",
            "running total",
            "moving average",
            "gaps and islands",
            "consecutive records",
            "top n",
            "median salary",
            "employees earning more than manager",
            "department highest salary"
        ]
    ),

    (
        "architecture",
        [

            "architecture",
            "software architecture",
            "solution architecture",
            "system architecture",
            "application architecture",
            "cloud architecture",

            "system design",
            "high level design",
            "low level design",
            "hld",
            "lld",

            "aws architecture",
            "azure architecture",
            "gcp architecture",

            "microservices architecture",
            "monolithic architecture",
            "event driven architecture",

            "component diagram",
            "sequence diagram",
            "deployment diagram",
            "class diagram",
            "activity diagram",
            "use case diagram",

            "data flow diagram",
            "dfd",

            "architecture diagram",
            "deployment architecture",
            "network architecture",
            "integration architecture"

        ]
    )
        ]

def classify_artifact(
        requirement,
        uploaded_document=""
):
    print("================================")
    print("CLASSIFIER INPUT")
    print(requirement)
    print("================================")

    requirement = requirement.lower()

    if uploaded_document.strip():

        if any(keyword in requirement for keyword in [

            "summarize",
            "summary",
            "extract",
            "analyze",
            "analyse",
            "review",
            "document",
            "explain",
            "key points",
            "highlights"

        ]):
            return "document_summary"


    # ---------------------------------
    # Priority Rule Engine
    # ---------------------------------

    for artifact, keywords in RULES:

        if match(requirement, keywords):
            print("=" * 60)
            print("RULE MATCHED")
            print(artifact)
            print("=" * 60)

            return artifact

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
        return "database_sql"

    elif "stored procedure" in requirement:
        return "database_sql"


    elif any(keyword in requirement for keyword in [
        "rtm",
        "requirements traceability matrix",
        "requirement traceability matrix",
        "traceability matrix"
    ]):
        return "requirement"

    elif any(keyword in requirement for keyword in [
        "generate sql function",
        "create sql function",
        "sql function"
    ]):
        return "database_sql"

    elif any(keyword in requirement for keyword in [
        "generate view",
        "create view",
        "sql view"
    ]):
        return "database_sql"

    elif any(keyword in requirement for keyword in [
        "generate trigger",
        "create trigger",
        "sql trigger"
    ]):
        return "database_sql"

    elif any(keyword in requirement for keyword in [
        "generate pom",
        "create pom",
        "page object model",
        "pom"
    ]):

        return "automation"

    elif any(keyword in requirement for keyword in [

        "devops",
        "docker",
        "docker compose",
        "kubernetes",
        "helm",
        "terraform",
        "ansible",
        "jenkins",
        "github actions",
        "gitlab ci",
        "azure devops",
        "aws codepipeline",
        "aws codebuild",
        "aws codedeploy",
        "argocd",
        "fluxcd",
        "pipeline",
        "ci/cd",
        "cicd",
        "deployment",
        "infrastructure as code"

    ]):
        return "devops"

    elif any(keyword in requirement for keyword in [
        "automation",
        "selenium",
        "playwright",
        "appium",
        "cypress",
        "pytest",
        "testng",
        "junit",
        "robot framework",
        "cucumber",
        "bdd",
        "page object model",
        "pom",
        "page factory",
        "data driven framework",
        "keyword driven framework",
        "hybrid framework",
        "modular framework",
        "framework",
        "automation framework",
        "automation script",
        "mobile automation",
        "web automation",
        "desktop automation",
        "winappdriver",
        "selenium grid",
        "browserstack",
        "lambdatest",
        "parallel execution",
        "automation architecture"
    ]):
        return "automation"

    elif any(keyword in requirement for keyword in [

        "python",
        "java",
        "c#",
        "c++",
        "javascript",
        "typescript",
        "react",
        "angular",
        "node",
        "express",
        "spring boot",
        "fastapi",
        "flask",
        "django",
        ".net",
        "html",
        "css",

        "code",
        "generate code",
        "write code",
        "implement",
        "algorithm",
        "data structure",
        "design pattern",
        "solid",
        "oop",
        "refactor",
        "graph",
        "tree",
        "linked list",
        "stack",
        "queue",
        "binary search",
        "dynamic programming",
        "leetcode",
        "graphql",
        "rest api",

        "singleton",
        "factory",
        "builder",
        "observer",
        "strategy",
        "decorator",
        "adapter",
        "prototype",

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

    print("=" * 60)
    print("DEFAULT")
    print("full_suite")
    print("=" * 60)

    return "full_suite"

