# agents/domain_classifier_agent.py

def classify_domain(requirement):

    requirement = requirement.lower()

    if any(word in requirement for word in [
        "claim",
        "policy",
        "premium",
        "insurance"
    ]):
        return "insurance"

    elif any(word in requirement for word in [
        "patient",
        "therapy",
        "medical",
        "health",
        "hospital"
        "ctm",
        "ins",
        "neurosense",
        "adaptivestim",
        "mri",
        "pain rc",
        "stim"
    ]):
        return "healthcare"

    elif any(word in requirement for word in [
        "product",
        "cart",
        "checkout",
        "order"
    ]):
        return "ecommerce"

    elif any(word in requirement for word in [
        "etl",
        "data warehouse",
        "dwh"
    ]):
        return "etl"

    elif any(word in requirement for word in [
        "salesforce",
        "crm"
    ]):
        return "salesforce"

    elif any(word in requirement for word in [
        "aws",
        "lambda",
        "s3"
    ]):
        return "aws"

    return "general"