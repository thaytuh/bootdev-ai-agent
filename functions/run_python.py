import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        result = subprocess.run(
            ["python", full_path], 
            timeout=30, 
            capture_output=True, 
            text=True,
            cwd=abs_working_dir
        )
        if result.returncode != 0:
            print(f'Process exited with code {result.returncode}:\n{result.stderr}')
            print(f'Return code for this error is {result.returncode}')
        if not result.stdout:
            return "No output produced."
        print(f'STDOUT: {result.stdout}')
        print(f'STDERR: {result.stderr}')
        return result.stdout
    except Exception as e:
        return f"Error executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specificed Python file and returns the output. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
        },
    ),
)