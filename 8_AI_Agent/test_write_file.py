
from functions.write_file import write_file


def main():
    # Test 1: Overwrite an existing file.
    print("Test 1: Overwrite lorem.txt")
    print(
        write_file(
            "calculator",
            "lorem.txt",
            "wait, this isn't lorem ipsum"
        )
    )

    # Test 2: Write to a file inside a nested directory.
    print("\nTest 2: Create morelorem.txt")
    print(
        write_file(
            "calculator",
            "pkg/morelorem.txt",
            "lorem ipsum dolor sit amet"
        )
    )

    # Test 3: Try writing outside the working directory.
    print("\nTest 3: Write outside the working directory")
    print(
        write_file(
            "calculator",
            "/tmp/temp.txt",
            "this should not be allowed"
        )
    )


if __name__ == "__main__":
    main()
