from config import MAX_CHARS
import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string)>MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and return the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
    ),
)