# generators/cicd_generator.py

from generators.jenkins_generator import (
    generate_jenkins_pipeline
)

from generators.github_actions_generator import (
    generate_github_actions
)

from generators.azure_devops_generator import (
    generate_azure_pipeline
)


def generate_cicd(requirement):

    req = requirement.lower()

    if "jenkins" in req:
        return generate_jenkins_pipeline(
            requirement
        )

    elif any(tool in req for tool in [
        "github",
        "github actions"
    ]):
        return generate_github_actions(
            requirement
        )

    elif any(tool in req for tool in [
        "azure",
        "azure devops"
    ]):
        return generate_azure_pipeline(
            requirement
        )

    return generate_jenkins_pipeline(
        requirement
    )