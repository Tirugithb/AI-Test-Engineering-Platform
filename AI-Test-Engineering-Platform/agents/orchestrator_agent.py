from agents.artifact_classifier_agent import (
    classify_artifact
)

from agents.test_case_agent import run as test_case_agent
from agents.test_plan_agent import run as test_plan_agent
from agents.test_strategy_agent import run as test_strategy_agent
from agents.automation_agent import run as automation_agent

from generators.sql_generator import (
    generate_sql
)

from generators.stored_procedure_generator import (
    generate_stored_procedure
)

from generators.function_generator import (
    generate_function
)

from generators.view_generator import (
    generate_view
)

from generators.trigger_generator import (
    generate_trigger
)

from generators.pom_generator import (
    generate_pom
)

from generators.rtm_generator import (
    generate_rtm
)

from generators.cicd_generator import (
    generate_cicd
)

from generators.defect_report_generator import (
    generate_defect_report
)

from generators.test_summary_report_generator import (
    generate_test_summary_report
)

from generators.release_report_generator import (
    generate_release_report
)

from generators.test_metrics_generator import (
    generate_test_metrics
)

from generators.code_generator import generate_code

from agents.document_agent import run as document_agent
from agents.requirement_agent import run as requirement_agent
from agents.api_agent import run as api_agent
from agents.database_agent import run as database_agent
from agents.architecture_agent import run as architecture_agent
from agents.devops_agent import run as devops_agent
from agents.code_generation_agent import run as code_generation_agent

def execute(
        requirement,
        uploaded_document=""
):
    artifact = classify_artifact(
        requirement,
        uploaded_document
    )

    print("=" * 60)
    print("UPLOADED DOCUMENT LENGTH")
    print(len(uploaded_document))
    print("=" * 60)

    print("=" * 60)
    print("REQUIREMENT")
    print(requirement)
    print("=" * 60)

    print("DETECTED ARTIFACT:")
    print(artifact)
    print("=" * 60)

    # Requirement Agent Routing
    if artifact == "requirement":

        if "brd" in requirement.lower():
            artifact = "brd"

        elif "frs" in requirement.lower():
            artifact = "frs"

        elif "user story" in requirement.lower():
            artifact = "user_story"

        elif "acceptance criteria" in requirement.lower():
            artifact = "acceptance_criteria"

        elif "use case" in requirement.lower():
            artifact = "use_case"

        elif "epic" in requirement.lower():
            artifact = "epic"

        elif "functional requirements" in requirement.lower():
            artifact = "functional_requirements"

        elif "non functional requirements" in requirement.lower() or \
                "non-functional requirements" in requirement.lower():
            artifact = "non_functional_requirements"

    # print(f"\nDetected Artifact: {artifact}")

    if artifact == "sql_query":

        return {
            "artifact": "sql_query",
            "sql": generate_sql(requirement)
        }

    elif artifact == "test_cases":

        return {
            "artifact": "test_cases",
            "test_case": test_case_agent(requirement)
        }

    elif artifact == "test_plan":

        return {
            "artifact": "test_plan",
            "test_plan": test_plan_agent(requirement)
        }

    elif artifact == "test_strategy":

        return {
            "artifact": "test_strategy",
            "test_strategy": test_strategy_agent(requirement)
        }

    elif artifact == "automation":

        return {

            "artifact": "automation",

            "automation":

                automation_agent(

                    requirement,

                    "automation"

                )

        }

    elif artifact == "api":

        if "postman" in requirement.lower():
            artifact = "postman_collection"

        elif "rest assured" in requirement.lower():
            artifact = "rest_assured"

        elif "swagger" in requirement.lower():
            artifact = "swagger"

        elif "openapi" in requirement.lower():
            artifact = "openapi"

        else:
            artifact = "api_test_cases"

        return {

            "artifact": artifact,

            artifact: api_agent(
                requirement,
                artifact
            )

        }

    elif artifact == "devops":

        return {

            "artifact": "devops",

            "devops":

                devops_agent(

                    requirement,

                    "devops"

                )

        }

    elif artifact == "stored_procedure":

        return {
            "artifact": "stored_procedure",
            "stored_procedure":
                generate_stored_procedure(
                    requirement
                )
        }

    elif artifact == "function":

        return {
            "artifact": "function",
            "function":
                generate_function(
                    requirement
                )
        }

    elif artifact == "view":

        return {
            "artifact": "view",
            "view": generate_view(
                requirement
            )
        }

    elif artifact == "trigger":

        return {
            "artifact": "trigger",
            "trigger":
                generate_trigger(
                    requirement
                )
        }

    # elif artifact == "er_diagram":
    #
    #     return {
    #
    #         "artifact": "er_diagram",
    #
    #         "er_diagram":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "er_diagram"
    #
    #             )
    #
    #     }
    #
    #
    # elif artifact == "database_schema":
    #
    #     return {
    #
    #         "artifact": "database_schema",
    #
    #         "database_schema":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "database_schema"
    #
    #             )
    #
    #     }
    #
    #
    # elif artifact == "table_design":
    #
    #     return {
    #
    #         "artifact": "table_design",
    #
    #         "table_design":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "table_design"
    #
    #             )
    #
    #     }
    #
    #
    # elif artifact == "data_dictionary":
    #
    #     return {
    #
    #         "artifact": "data_dictionary",
    #
    #         "data_dictionary":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "data_dictionary"
    #
    #             )
    #
    #     }
    #
    #
    # elif artifact == "sample_data":
    #
    #     return {
    #
    #         "artifact": "sample_data",
    #
    #         "sample_data":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "sample_data"
    #
    #             )
    #
    #     }
    #
    #
    # elif artifact == "database_optimization":
    #
    #     return {
    #
    #         "artifact": "database_optimization",
    #
    #         "database_optimization":
    #
    #             database_agent(
    #
    #                 requirement,
    #
    #                 "database_optimization"
    #
    #             )
    #
    #     }
    #
    # elif artifact == "index_recommendation":
    #
    #     return {
    #         "artifact": "index_recommendation",
    #         "index_recommendation":
    #             database_agent(
    #                 requirement,
    #                 "index_recommendation"
    #             )
    #     }
    #
    # elif artifact == "normalization":
    #
    #     return {
    #         "artifact": "normalization",
    #         "normalization":
    #             database_agent(
    #                 requirement,
    #                 "normalization"
    #             )
    #     }
    #
    # elif artifact == "partition_strategy":
    #
    #     return {
    #         "artifact": "partition_strategy",
    #         "partition_strategy":
    #             database_agent(
    #                 requirement,
    #                 "partition_strategy"
    #             )
    #     }
    #
    # elif artifact == "migration_script":
    #
    #     return {
    #         "artifact": "migration_script",
    #         "migration_script":
    #             database_agent(
    #                 requirement,
    #                 "migration_script"
    #             )
    #     }

    elif artifact in [

        "er_diagram",
        "database_schema",
        "table_design",
        "data_dictionary",
        "sample_data",
        "database_optimization",
        "index_recommendation",
        "normalization",
        "partition_strategy",
        "migration_script",
        "database_sql"

    ]:

        return {

            "artifact": artifact,

            artifact:

                database_agent(

                    requirement,

                    artifact

                )

        }

    elif artifact == "pom":

        return {
            "artifact": "pom",
            "pom": generate_pom(
                requirement
            )
        }

    elif artifact == "rtm":

        return {
            "artifact": "rtm",
            "rtm": generate_rtm(
                requirement
            )
        }

    elif artifact == "cicd":

        return {
            "artifact": "cicd",
            "cicd": generate_cicd(
                requirement
            )
        }

    elif artifact == "defect_report":

        return {
            "artifact": "defect_report",
            "defect_report":
                generate_defect_report(
                    requirement
                )
        }

    elif artifact == "test_summary_report":

        return {
            "artifact": "test_summary_report",
            "test_summary_report":
                generate_test_summary_report(
                    requirement
                )
        }

    elif artifact == "release_report":

        return {
            "artifact": "release_report",
            "release_report":
                generate_release_report(
                    requirement
                )
        }

    elif artifact in [

        "document",
        "document_analysis",
        "document_summary",
        "document_requirements",
        "document_risks",
        "document_actions"

    ]:

        return {

            "artifact": artifact,

            artifact:

                document_agent(

                    requirement,

                    artifact

                )

        }


    elif artifact == "test_metrics":

        return {
            "artifact": "test_metrics",
            "test_metrics":
                generate_test_metrics(
                    requirement
                )
        }

    elif artifact in [

        "brd",
        "frs",
        "user_story",
        "acceptance_criteria",
        "use_case",
        "epic",
        "functional_requirements",
        "non_functional_requirements"

    ]:

        return {

            "artifact": artifact,

            artifact:

                requirement_agent(

                    requirement,

                    artifact

                )

        }

    elif artifact in [

        "api_test_cases",
        "postman_collection",
        "rest_assured",
        "swagger",
        "openapi"

    ]:

        return {

            "artifact": artifact,

            artifact:

                api_agent(

                    requirement,

                    artifact

                )

        }


    elif artifact == "architecture":

        return {

            "artifact": "architecture",

            "architecture":

                architecture_agent(

                    requirement,

                    "architecture"

                )

        }

    elif artifact == "code_generation":

        return {

            "artifact": "code_generation",

            "code_generation":

                code_generation_agent(

                    requirement,

                    "code_generation"

                )

        }

    # Default Full Suite

    return {
        "artifact": "full_suite",
        "test_case": test_case_agent(requirement),
        "test_plan": test_plan_agent(requirement),
        "test_strategy": test_strategy_agent(requirement),
        "automation": automation_agent(requirement)
    }