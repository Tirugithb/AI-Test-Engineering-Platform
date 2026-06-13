import sys
import os
import time

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)


import streamlit as st

# ADD HERE
if "messages" not in st.session_state:
    st.session_state.messages = []

if "download_content" not in st.session_state:
    st.session_state.download_content = ""

if "download_file_name" not in st.session_state:
    st.session_state.download_file_name = ""

if "response_count" not in st.session_state:
    st.session_state.response_count = 0

if "document_count" not in st.session_state:
    st.session_state.document_count = 0

from agents.orchestrator_agent import execute

# ==================================================
# PAGE CONFIG
# ==================================================

st.markdown("""
<style>

/* Move chat input to bottom */
.stChatInput {
    position: fixed;
    bottom: 20px;
    left: 420px;
    right: 220px;
    z-index: 999;
}

/* Rounded */
.stChatInput > div {
    border-radius: 999px !important;
}

/* Leave space for chat */
.main .block-container {
    padding-bottom: 100px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🤖 TestGen AI")

    st.markdown("---")

    st.subheader("AI Agents")

    st.markdown("""
### QA Agent
- Test Cases
- Test Scenarios
- Test Plan
- Test Strategy
- Defect Report
- Test Metrics

### Requirement Agent
- BRD
- FRS
- User Stories
- Acceptance Criteria
- Use Cases
- Epics

### API Agent
- API Test Cases
- Postman Collection
- REST Assured
- Swagger
- OpenAPI

### Automation Agent
- Selenium
- Playwright
- Appium
- Automation Framework

### Database Agent
- SQL
- ER Diagram
- Database Schema
- Table Design
- Data Dictionary
- Optimization

### Architecture Agent
- HLD
- LLD
- Solution Architecture
- System Architecture

### DevOps Agent
- Docker
- Kubernetes
- Terraform
- Jenkins
- GitHub Actions

### Code Generation Agent
- Python
- Java
- React
- Spring Boot
- FastAPI
- Design Patterns
""")


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<h1 style='text-align:center; color:#1f77b4; font-size:55px;'>
🤖 TestGen AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:22px; color:#555555;'>
AI-Powered Test Engineering Assistant
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:16px; color:#777777;'>
Accelerate software delivery with AI agents that generate QA, Automation, Database, and DevOps assets from natural language requirements.
</p>
""", unsafe_allow_html=True)

# Add space below title

st.markdown(
    "<div style='height:40px;'></div>",
    unsafe_allow_html=True
)


st.markdown("### Try these examples")

c1, c2 = st.columns(2)


with c1:
    st.info("Generate BRD for Hospital Management System")
    st.info("Generate Test Cases for Login Screen")
    st.info("Generate API Test Cases for User API")
    st.info("Generate ER Diagram for Banking System")

with c2:
    st.info("Generate Selenium Automation Script")
    st.info("Generate DevOps Architecture for E-commerce")
    st.info("Generate Dockerfile for FastAPI")
    st.info("Generate Python Singleton Pattern")

# ==========================================
# INPUT AREA
# ==========================================

st.markdown("""
<style>

/* Hide drag-drop text */
[data-testid="stFileUploaderDropzoneInstructions"] {
    display: none;
}

/* Make uploader look like attachment button */
[data-testid="stFileUploader"] {
    position: fixed;
    bottom: 28px;
    right: 110px;
    width: 45px;
    z-index: 1000;
}

[data-testid="stFileUploaderDropzone"] {
    min-height: 40px !important;
    padding: 0px !important;
    border: none !important;
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader(
    "📎",
    type=["pdf", "docx", "txt", "xlsx"],
    label_visibility="collapsed"
)

# Extract file content
file_text = ""

if uploaded_file is not None:

    st.session_state.document_count += 1

    # TXT
    if uploaded_file.name.endswith(".txt"):
        file_text = uploaded_file.read().decode("utf-8")

    # PDF
    elif uploaded_file.name.endswith(".pdf"):

        from pypdf import PdfReader

        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            text = page.extract_text()
            if text:
                file_text += text + "\n"

    # DOCX
    elif uploaded_file.name.endswith(".docx"):

        from docx import Document

        doc = Document(uploaded_file)

        for para in doc.paragraphs:
            file_text += para.text + "\n"

    st.success(f"Uploaded: {uploaded_file.name}")
    st.write("Characters extracted:", len(file_text))

    with st.expander("Preview File Content"):
        st.code(file_text[:2000])

# ==================================================
# CHAT HISTORY
# ==================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# DOWNLOAD BUTTON
if st.session_state.download_content:

    st.download_button(
        label="📥 Download Output",
        data=st.session_state.download_content,
        file_name=st.session_state.download_file_name,
        mime="text/plain"
    )

# ==================================================
# INPUT SECTION
# ==================================================

requirement = st.chat_input(
    "Ask anything..."
)

generate = bool(requirement)


# ==================================================
# GENERATE
# ==================================================

if generate:

    final_requirement = f"""
    USER REQUEST:

    {requirement}

    ==================================

    UPLOADED DOCUMENT:

    {file_text}
    """

    # ---------- ADD THIS BLOCK HERE ----------
    if uploaded_file is None and requirement:

        doc_keywords = [
            "uploaded document",
            "uploaded file",
            "uploaded resume"
        ]

        if any(word in requirement.lower() for word in doc_keywords):
            st.warning("Please upload a document first.")
            st.stop()
    # ---------- END OF BLOCK ----------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": requirement
        }
    )

    debug = st.sidebar.checkbox("Show Debug Information")

    with st.spinner("Generating artifact..."):

        if debug:
            st.write("Requirement:")
            st.code(requirement)

            st.write("First 500 chars of final_requirement:")
            st.code(final_requirement[:500])

        uploaded_document = ""

        if uploaded_file is not None:
            uploaded_document = uploaded_file.read().decode("utf-8", errors="ignore")

        start_time = time.time()

        try:
            results = execute(
                final_requirement,
                uploaded_document
            )

            end_time = time.time()

            execution_time = round(
                end_time - start_time,
                2
            )

        except Exception as e:
            st.error(f"Error: {e}")
            import traceback

            st.code(traceback.format_exc())
            st.stop()

        artifact = results["artifact"]

        AGENT_NAMES = {
            "requirement": "Requirement Agent",
            "test_cases": "QA Agent",
            "api": "API Agent",
            "automation": "Automation Agent",
            "database_sql": "Database Agent",
            "architecture": "Architecture Agent",
            "devops": "DevOps Agent",
            "code_generation": "Code Generation Agent",
            "document_summary": "Document Agent",
        }

        agent_name = AGENT_NAMES.get(
            artifact,
            "AI Agent"
        )

        st.success("✅ Generation Completed")

        st.markdown(
            f"## 🤖 {agent_name}"
        )

        st.markdown(
            f"**🏷️ Artifact:** `{artifact}`"
        )

        st.info(
            f"⏱ Response Time : {execution_time} sec"
        )

    response_text = ""
    download_content = ""
    download_file_name = "output.txt"

    ARTIFACT_MAPPING = {

        "automation": (
            "automation",
            "Automation.md"
        ),

        "devops": (
            "devops",
            "DevOps.md"
        ),

        "code_generation": (
            "code_generation",
            "Code_Generation.md"
        ),

        "architecture": (
            "architecture",
            "Architecture.md"
        ),

        "database_sql": (
            "database_sql",
            "Database_SQL.md"
        ),

        "document_summary": (
            "document_summary",
            "Document_Summary.txt"
        ),

        "api_test_cases": (
            "api_test_cases",
            "API_Test_Cases.txt"
        ),

        "test_cases": (
            "test_case",
            "Test_Cases.txt"
        ),

        "test_plan": (
            "test_plan",
            "Test_Plan.txt"
        ),

        "test_strategy": (
            "test_strategy",
            "Test_Strategy.txt"
        ),

        "brd": (
            "brd",
            "BRD.txt"
        ),

        "frs": (
            "frs",
            "FRS.txt"
        ),

        "user_story": (
            "user_story",
            "UserStories.txt"
        ),

        "acceptance_criteria": (
            "acceptance_criteria",
            "AcceptanceCriteria.txt"
        ),

        "use_case": (
            "use_case",
            "Use_Cases.txt"
        ),

        "epic": (
            "epic",
            "Epics.txt"
        ),
    }

    # ==========================================
    # COMMON RESPONSE HANDLER
    # ==========================================

    def save_response(content, filename):

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": content
            }
        )
        st.session_state.response_count += 1

        return content, filename


    # ==========================================
    # AUTOMATION AGENT
    # ==========================================

    if artifact == "automation":

        response_text, download_file_name = save_response(
            results["automation"],
            "Automation.md"
        )

        download_content = response_text

    # ==========================================
    # DEVOPS AGENT
    # ==========================================


    elif artifact == "devops":

        response_text, download_file_name = save_response(
            results["devops"],
            "DevOps.md"
        )

        download_content = response_text

    # ==========================================
    # CODE GENERATION AGENT
    # ==========================================


    elif artifact == "code_generation":

        response_text, download_file_name = save_response(
            results["code_generation"],
            "Code_Generation.md"
        )

        download_content = response_text

    # ==========================================
    # DEFECT REPORT
    # ==========================================

    elif artifact == "defect_report":

        response_text = results["defect_report"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Defect_Report.txt"

    # ==========================================
    # TEST SUMMARY REPORT
    # ==========================================

    elif artifact == "test_summary_report":

        response_text = results["test_summary_report"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Test_Summary_Report.txt"

    # ==========================================
    # RELEASE REPORT
    # ==========================================

    elif artifact == "release_report":

        response_text = results["release_report"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Release_Report.txt"

    # ==========================================
    # TEST METRICS
    # ==========================================

    elif artifact == "test_metrics":

        response_text = results["test_metrics"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Test_Metrics.txt"

    # ==========================================
    # TEST CASES
    # ==========================================

    elif artifact == "test_cases":

        response_text = results["test_case"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Test_Cases.txt"

    # ==========================================
    # TEST PLAN
    # ==========================================

    elif artifact == "test_plan":

        response_text = results["test_plan"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Test_Plan.txt"

    # ==========================================
    # TEST STRATEGY
    # ==========================================

    elif artifact == "test_strategy":

        response_text = results["test_strategy"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Test_Strategy.txt"

    # ==========================================
    # Document Analysis
    # ==========================================

    elif artifact == "document_analysis":

        response_text = results["analysis"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Document_Analysis.txt"

    elif artifact == "document_summary":

        response_text = results["document_summary"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Document_Summary.txt"


    elif artifact == "document_requirements":

        response_text = results["requirements"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Requirements.txt"


    elif artifact == "document_risks":

        response_text = results["risks"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Document_Risks.txt"


    elif artifact == "document_actions":

        response_text = results["actions"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Action_Items.txt"


    # # ==========================================
    # # Python Code
    # # ==========================================
    # elif artifact == "python_code":
    #
    #     response_text = f"```python\n{results['python']}\n```"
    #
    #     st.session_state.messages.append(
    #         {
    #             "role": "assistant",
    #             "content": response_text
    #         }
    #     )
    #
    #     download_content = results["python"]
    #     download_file_name = "Python_Code.py"

    elif artifact == "brd":

        response_text = results["brd"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "BRD.txt"

    elif artifact == "frs":

        response_text = results["frs"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "FRS.txt"

    elif artifact == "user_story":

        response_text = results["user_story"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "UserStories.txt"

    elif artifact == "acceptance_criteria":

        response_text = results["acceptance_criteria"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "AcceptanceCriteria.txt"

    # ==========================================
    # USE CASE
    # ==========================================

    elif artifact == "use_case":

        response_text = results["use_case"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Use_Cases.txt"

    # ==========================================
    # EPIC
    # ==========================================

    elif artifact == "epic":

        response_text = results["epic"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Epics.txt"

    # ==========================================
    # FUNCTIONAL REQUIREMENTS
    # ==========================================

    elif artifact == "functional_requirements":

        response_text = results["functional_requirements"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Functional_Requirements.txt"

    # ==========================================
    # NON FUNCTIONAL REQUIREMENTS
    # ==========================================

    elif artifact == "non_functional_requirements":

        response_text = results["non_functional_requirements"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Non_Functional_Requirements.txt"

    # ==========================================
    # API TEST CASES
    # ==========================================

    elif artifact == "api_test_cases":

        response_text = results["api_test_cases"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "API_Test_Cases.txt"


    # ==========================================
    # POSTMAN COLLECTION
    # ==========================================

    elif artifact == "postman_collection":

        response_text = results["postman_collection"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Postman_Collection.txt"


    # ==========================================
    # REST ASSURED
    # ==========================================

    elif artifact == "rest_assured":

        response_text = results["rest_assured"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "REST_Assured_Framework.txt"


    # ==========================================
    # SWAGGER
    # ==========================================

    elif artifact == "swagger":

        response_text = results["swagger"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Swagger_Specification.txt"


    # ==========================================
    # OPENAPI
    # ==========================================

    elif artifact == "openapi":

        response_text = results["openapi"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "OpenAPI_Specification.yaml"

    # ==========================================
    # ER DIAGRAM
    # ==========================================

    elif artifact == "er_diagram":

        response_text = results["er_diagram"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "ER_Diagram.txt"

    # ==========================================
    # DATABASE SCHEMA
    # ==========================================

    elif artifact == "database_schema":

        response_text = results["database_schema"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Database_Schema.txt"

    # ==========================================
    # TABLE DESIGN
    # ==========================================

    elif artifact == "table_design":

        response_text = results["table_design"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Table_Design.txt"

    # ==========================================
    # DATA DICTIONARY
    # ==========================================

    elif artifact == "data_dictionary":

        response_text = results["data_dictionary"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Data_Dictionary.txt"

    # ==========================================
    # SAMPLE DATA
    # ==========================================

    elif artifact == "sample_data":

        response_text = results["sample_data"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Sample_Data.txt"

    # ==========================================
    # DATABASE OPTIMIZATION
    # ==========================================

    elif artifact == "database_optimization":

        response_text = results["database_optimization"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Database_Optimization.txt"

    elif artifact == "index_recommendation":

        response_text = results["index_recommendation"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Index_Recommendation.txt"

    elif artifact == "normalization":

        response_text = results["normalization"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Normalization.txt"

    elif artifact == "partition_strategy":

        response_text = results["partition_strategy"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Partition_Strategy.txt"

    elif artifact == "migration_script":

        response_text = results["migration_script"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Migration_Script.sql"

    # ==========================================
    # DATABASE SQL
    # ==========================================

    elif artifact == "database_sql":

        response_text = results["database_sql"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Database_SQL.md"


    elif artifact == "architecture":

        response_text = results["architecture"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_text
            }
        )

        download_content = response_text
        download_file_name = "Architecture.md"


    # ==========================================
    # DEFAULT
    # ==========================================

    else:

        st.json(results)

    # ==========================================
    # SAVE DOWNLOAD DATA
    # ==========================================

    st.session_state.download_content = download_content
    st.session_state.download_file_name = download_file_name

    st.rerun()