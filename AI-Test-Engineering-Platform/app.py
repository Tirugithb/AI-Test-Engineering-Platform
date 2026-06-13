# app.py

from agents.orchestrator_agent import execute
from analyzers.requirement_analyzer import analyze_requirement
from exporters.docx_exporter import export_to_docx


def main():
    print("=" * 50)
    print("AI TEST ENGINEERING AGENT")
    print("=" * 50)

    requirement = input("\nEnter Requirement: ")

    flow_type = analyze_requirement(requirement)

    print("\n" + "=" * 50)
    print("REQUIREMENT ANALYSIS")
    print("=" * 50)
    print(f"Detected Flow: {flow_type}")

    # Execute all agents
    results = execute(requirement)
    artifact = results["artifact"]

    # SQL Query

    if artifact == "sql_query":
        sql_output = results["sql"]

        print("\nGenerated SQL Query:\n")
        print(sql_output)

        with open(
                "output/SQL_Query.sql",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(sql_output)

        print("\nSQL Query saved successfully.")
        print("Location: output/SQL_Query.sql")

        return

    # stored_procedure

    elif artifact == "stored_procedure":

        sp = results["stored_procedure"]

        print("\nGenerated Stored Procedure:\n")
        print(sp)

        with open(
                "output/Stored_Procedure.sql",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(sp)

        print("\nStored Procedure saved successfully.")
        print(
            "Location: output/Stored_Procedure.sql"
        )

        return

    # function

    elif artifact == "function":

        function_sql = results["function"]

        print("\nGenerated Function:\n")
        print(function_sql)

        with open(
                "output/Function.sql",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(function_sql)

        print("\nFunction saved successfully.")
        print("Location: output/Function.sql")

        return

    # view

    elif artifact == "view":

        view_sql = results["view"]

        print("\nGenerated View:\n")
        print(view_sql)

        with open(
                "output/View.sql",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(view_sql)

        print("\nView saved successfully.")
        print("Location: output/View.sql")

        return

    # trigger

    elif artifact == "trigger":

        trigger_sql = results["trigger"]

        print("\nGenerated Trigger:\n")
        print(trigger_sql)

        with open(
                "output/Trigger.sql",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(trigger_sql)

        print("\nTrigger saved successfully.")
        print("Location: output/Trigger.sql")

        return

    # pom (Page Object Model)

    elif artifact == "pom":

        pom_code = results["pom"]

        print("\nGenerated POM:\n")
        print(pom_code)

        with open(
                "output/POM.py",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(pom_code)

        print("\nPOM saved successfully.")
        print("Location: output/POM.py")

        return

    #rtm(Requirements Traceability Matrix)
    elif artifact == "rtm":

        rtm = results["rtm"]

        print("\nGenerated RTM:\n")
        print(rtm)

        with open(
                "output/RTM.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(rtm)

        export_to_docx(
            rtm,
            "output/RTM.docx"
        )

        print("\nRTM saved successfully.")
        print("Location: output/RTM.txt")

        return

    #CI/CD Pipeline

    elif artifact == "cicd":

        pipeline = results["cicd"]

        print("\nGenerated CI/CD Pipeline:\n")
        print(pipeline)

        with open(
                "output/CICD_Pipeline.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(pipeline)

        print("\nCI/CD Pipeline saved successfully.")
        print(
            "Location: output/CICD_Pipeline.txt"
        )

        return
    # Defect Report

    elif artifact == "defect_report":

        report = results["defect_report"]

        print("\nGenerated Defect Report:\n")
        print(report)

        with open(
                "output/Defect_Report.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(report)

        export_to_docx(
            report,
            "output/Defect_Report.docx"
        )

        print("\nDefect Report saved successfully.")

        return
    # Test Summary Report

    elif artifact == "test_summary_report":

        report = results[
            "test_summary_report"
        ]

        print(
            "\nGenerated Test Summary Report:\n"
        )

        print(report)

        with open(
                "output/Test_Summary_Report.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(report)

        export_to_docx(
            report,
            "output/Test_Summary_Report.docx"
        )

        print(
            "\nTest Summary Report saved successfully."
        )

        return

    # Release Report

    elif artifact == "release_report":

        report = results["release_report"]

        print("\nGenerated Release Report:\n")
        print(report)

        with open(
                "output/Release_Report.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(report)

        export_to_docx(
            report,
            "output/Release_Report.docx"
        )

        print("\nRelease Report saved successfully.")

        return
    # Test Metrics

    elif artifact == "test_metrics":

        report = results["test_metrics"]

        print("\nGenerated Test Metrics:\n")
        print(report)

        with open(
                "output/Test_Metrics.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(report)

        export_to_docx(
            report,
            "output/Test_Metrics.docx"
        )

        print("\nTest Metrics saved successfully.")

        return

    # Test Cases

    elif artifact == "test_cases":

        test_case = results["test_case"]

        print("\nGenerated Test Case:\n")
        print(test_case)

        with open(
                "output/Test_Cases.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(test_case)

        export_to_docx(
            test_case,
            "output/Test_Cases.docx"
        )

        print("\nTest case saved successfully.")
        print("Location: output/Test_Cases.txt")

        return

    # Test Plan

    elif artifact == "test_plan":

        test_plan = results["test_plan"]

        print("\nGenerated Test Plan:\n")
        print(test_plan)

        with open(
                "output/Test_Plan.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(test_plan)

        export_to_docx(
            test_plan,
            "output/Test_Plan.docx"
        )

        print("\nTest plan saved successfully.")
        print("Location: output/Test_Plan.txt")

        return

    # Test Strategy

    elif artifact == "test_strategy":

        test_strategy = results["test_strategy"]

        print("\nGenerated Test Strategy:\n")
        print(test_strategy)

        with open(
                "output/Test_Strategy.txt",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(test_strategy)

        export_to_docx(
            test_strategy,
            "output/Test_Strategy.docx"
        )

        print("\nTest strategy saved successfully.")
        print("Location: output/Test_Strategy.txt")

        return

    # Automation Script

    elif artifact == "automation_script":

        automation_script = results["automation"]

        with open(
                "output/Automation_Script.py",
                "w",
                encoding="utf-8"
        ) as file:
            file.write(automation_script)

        print("\nAutomation script saved successfully.")
        print("Location: output/Automation_Script.py")

        return

    if artifact != "full_suite":
        return


    # Test Case
    test_case = results["test_case"]

    print("\nGenerated Test Case:\n")
    print(test_case)

    with open("output/Test_Cases.txt", "w", encoding="utf-8") as file:
        file.write(test_case)

    export_to_docx(
        test_case,
        "output/Test_Cases.docx"
    )

    print("\nTest case saved successfully.")
    print("Location: output/Test_Cases.txt")

    # Test Plan
    test_plan = results["test_plan"]

    print("\nGenerated Test Plan:\n")
    print(test_plan)

    with open("output/Test_Plan.txt", "w", encoding="utf-8") as file:
        file.write(test_plan)

    export_to_docx(
        test_plan,
        "output/Test_Plan.docx"
    )

    print("\nTest plan saved successfully.")
    print("Location: output/Test_Plan.txt")

    # Test Strategy
    test_strategy = results["test_strategy"]

    print("\nGenerated Test Strategy:\n")
    print(test_strategy)

    with open("output/Test_Strategy.txt", "w", encoding="utf-8") as file:
        file.write(test_strategy)

    export_to_docx(
        test_strategy,
        "output/Test_Strategy.docx"
    )

    print("\nTest strategy saved successfully.")
    print("Location: output/Test_Strategy.txt")

    # Automation Script
    automation_script = results["automation"]

    with open("output/Automation_Script.py", "w", encoding="utf-8") as file:
        file.write(automation_script)

    print("\nAutomation script saved successfully.")
    print("Location: output/Automation_Script.py")


if __name__ == "__main__":
    main()