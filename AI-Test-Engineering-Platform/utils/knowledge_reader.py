# utils/knowledge_reader.py

import os


def read_knowledge(file_name):

    base_path = "knowledge_base"

    file_path = os.path.join(base_path, file_name)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return ""