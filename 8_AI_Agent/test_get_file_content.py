
from functions.get_file_content import get_file_content


def main():
    # Test 1: Read a large file and check truncation.
    result = get_file_content("calculator", "lorem.txt")

    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    # Test 2: Read a smaller Python file.
    print("\nResult for main.py:")
    print(get_file_content("calculator", "main.py"))

    # Test 3: Read a file inside the pkg directory.
    print("\nResult for pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Test 4: Try reading a file outside the working directory.
    print("\nResult for /bin/cat:")
    print(get_file_content("calculator", "/bin/cat"))

    # Test 5: Try reading a file that does not exist.
    print("\nResult for missing file:")
    print(
        get_file_content(
            "calculator",
            "pkg/does_not_exist.py"
        )
    )


if __name__ == "__main__":
    main()
