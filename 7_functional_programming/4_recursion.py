# Recursion
# A recursive function calls itself with a smaller version of the problem.
#
# Every recursive function needs:
# 1. A base case to stop recursion.
# 2. A recursive case that moves toward the base case.


def factorial(number: int) -> int:
    if number <= 1:          # base case
        return 1

    return number * factorial(number - 1)  # recursive case


print(factorial(5))
# 120


# Each call works on a smaller value:
#
# factorial(5)
# -> 5 * factorial(4)
# -> 5 * 4 * factorial(3)
# -> 5 * 4 * 3 * factorial(2)
# -> 5 * 4 * 3 * 2 * factorial(1)
# -> 120


# Recursion can also process a collection
# by reducing the problem one item at a time.


def sum_numbers(numbers: list[int]) -> int:
    if not numbers:          # base case
        return 0

    return numbers[0] + sum_numbers(numbers[1:])


print(sum_numbers([1, 2, 3, 4]))
# 10

#! Recursion on Tree Structures
# Recursion is useful when the depth of a nested structure is unknown.
# Examples include file systems and nested dictionaries.


def list_files(
    directory: dict[str, dict | None],
    current_path: str = ""
) -> list[str]:
    file_paths = []

    for name, value in directory.items():
        path = f"{current_path}/{name}"

        if value is None:
            # Base case: this entry is a file.
            file_paths.append(path)
        else:
            # Recursive case: explore the child directory.
            child_paths = list_files(value, path)
            file_paths.extend(child_paths)

    return file_paths


files = {
    "docs": {
        "report.txt": None,
        "images": {
            "photo.png": None,
        },
    }
}

print(list_files(files))

#! Dangers of Recursion
# Recursive calls use stack memory, so very deep recursion
# can cause a stack overflow.
#
# A missing or incorrect base case can cause infinite recursion.
#
# In Python, recursion can also be slower than a loop because
# every recursive call has function-call overhead.
#
# Use recursion when it makes the problem clearer, especially
# for nested or tree-like data, but avoid it when a simple loop
# is more appropriate.