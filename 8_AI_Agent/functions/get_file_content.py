import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the contents of a file within the permitted working directory, with a maximum character limit",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
  try:

    working_dir_abs = os.path.abspath(working_directory)

    target_file = os.path.normpath(
        os.path.join(working_dir_abs, file_path)
    )

    valid_target = (
      os.path.commonpath([working_dir_abs, target_file])
      == working_dir_abs
    ) 

    if not valid_target:
      return (
          f'Error: Cannot read "{file_path}" as it is outside '
          "the permitted working directory"
      )

    if not os.path.isfile(target_file):
      return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(target_file, "r", encoding="utf-8") as f:
      content = f.read(MAX_CHARS)
      
      if f.read(1):
        content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content

  except Exception as e:
    return f"Error: {e}"