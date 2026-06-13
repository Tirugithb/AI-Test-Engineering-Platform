# test_docx_exporter.py

from exporters.docx_exporter import export_to_docx

sample_content = """
AI TEST ENGINEERING PLATFORM

Test Case ID: TC001

Test Case Name:
Validate Login Functionality

Priority:
High

Preconditions:
Application is available

Test Steps:
1. Launch application
2. Enter valid username
3. Enter valid password
4. Click Login

Expected Result:
User should be successfully logged in.
"""

export_to_docx(
    sample_content,
    "output/Test_Cases.docx"
)

print("DOCX export completed successfully.")