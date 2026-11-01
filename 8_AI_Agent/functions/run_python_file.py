import os
import subprocess

def run_python_file(
    working_directory: str,
    file_path: str,
    args: list[str] | None = None) -> str:
    try:
      working_dir_abs = os.path.abspath(working_directory)

      target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

      valid_target = (os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs)

      if not valid_target:
        return (
        f'Error: Cannot execute "{file_path}" as it is outside '
        "the permitted working directory")

      if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

      if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

      command = ["python", target_file]

      if args:
          command.extend(args)

      result = subprocess.run(
        command,
        cwd=working_dir_abs,
        capture_output=True,
        text=True,
        timeout=30
      )

      output = []

      if result.returncode != 0:
          output.append(
            f"Process exited with code {result.returncode}"
          )

      if result.stdout:
        output.append(f"STDOUT:\n{result.stdout}")

      if result.stderr:
        output.append(f"STDERR:\n{result.stderr}")

      if not result.stdout and not result.stderr:
        output.append("No output produced")

      return "\n".join(output)

    except Exception as e:
      return f"Error: executing Python file: {e}"


