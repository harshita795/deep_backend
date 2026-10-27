import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Convert the permitted working directory to an absolute path
        working_dir_abs = os.path.abspath(working_directory)

        # Construct and normalize the requested target path
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        # Check whether the target is inside the permitted directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir])
            == working_dir_abs
        )

        if not valid_target_dir:
            return (
                f'Error: Cannot list "{directory}" as it is outside '
                "the permitted working directory"
            )

        # Check that the target exists and is a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"
