from functions.run_python_file import run_python_file

def main():
    # Test 1: Run calculator without additional arguments.
    print("Test 1: Run calculator without arguments")
    print(
        run_python_file("calculator", "main.py")
    )

    # Test 2: Run calculator with an expression.
    print("\nTest 2: Run calculator with an expression")
    print(
        run_python_file(
            "calculator",
            "main.py",
            ["3 + 5"]
        )
    )

    # Test 3: Run calculator unit tests.
    print("\nTest 3: Run calculator tests")
    print(
        run_python_file("calculator", "tests.py")
    )

    # Test 4: Try to execute a file outside the working directory.
    print("\nTest 4: Execute outside working directory")
    print(
        run_python_file("calculator", "../main.py")
    )

    # Test 5: Try to execute a nonexistent file.
    print("\nTest 5: Execute nonexistent file")
    print(
        run_python_file("calculator", "nonexistent.py")
    )

    # Test 6: Try to execute a non-Python file.
    print("\nTest 6: Execute a text file")
    print(
        run_python_file("calculator", "lorem.txt")
    )


if __name__ == "__main__":
    main()
