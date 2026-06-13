from llm.openai_client import generate_ai_response

response = generate_ai_response(
    "Generate 5 test cases for Login Functionality"
)

print(response)