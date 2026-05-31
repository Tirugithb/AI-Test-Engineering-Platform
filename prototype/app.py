# AI Test Engineering Platform - Prototype V1

def generate_test_case(requirement):
    return f"""
========================================
AI GENERATED TEST CASE
========================================

Requirement:
{requirement}

Test Case ID:
TC_001

Test Case Name:
Validate {requirement}

Preconditions:
- Application is installed
- User has valid access

Test Steps:
1. Launch application
2. Navigate to target screen
3. Perform required action
4. Verify expected behavior

Expected Result:
Application behaves as expected.

Priority:
High

Test Type:
Functional
"""


if __name__ == "__main__":
    requirement = input("Enter Requirement: ")

    test_case = generate_test_case(requirement)

    print(test_case)

    with open("generated_test_case.txt", "w") as file:
        file.write(test_case)

    print("Test case generated successfully.")
