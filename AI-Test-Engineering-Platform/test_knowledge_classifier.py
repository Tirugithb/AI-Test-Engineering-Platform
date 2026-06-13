# test_knowledge_classifier.py

from agents.knowledge_classifier_agent import classify_requirement

print(
    classify_requirement(
        "Validate Login Functionality using Selenium"
    )
)

print(
    classify_requirement(
        "Validate Customer API"
    )
)

print(
    classify_requirement(
        "Validate Search Screen UI"
    )
)