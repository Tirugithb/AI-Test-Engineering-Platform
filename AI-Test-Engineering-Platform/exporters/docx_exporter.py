# exporters/docx_exporter.py

from docx import Document


def export_to_docx(content, file_name):
    """
    Export content to a DOCX file.

    Args:
        content (str): Content to write into the DOCX file.
        file_name (str): Output DOCX file path.
    """

    try:
        document = Document()

        # Add content
        document.add_paragraph(content)

        # Save file
        document.save(file_name)

        print(f"DOCX file created successfully: {file_name}")

    except Exception as e:
        print(f"Error creating DOCX file: {e}")