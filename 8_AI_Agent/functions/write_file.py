import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
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
                f'Error: Cannot write to "{file_path}" as it is outside '
                "the permitted working directory"
            )

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(target_file)

        os.makedirs(parent_dir, exist_ok=True)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" '
            f"({len(content)} characters written)"
        )

    except Exception as e:
        return f"Error: {e}"
