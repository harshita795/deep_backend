from collections.abc import Callable


# First-Class Functions
# Functions are values, so they can be assigned to variables
# and passed around like other data.


def double(number: int) -> int:
    return number * 2


operation = double

print(operation(5))


# Functions can be passed as arguments to other functions.

def apply_operation(
    number: int,
    operation: Callable[[int], int]
) -> int:
    return operation(number)


print(apply_operation(10, double))


# Callable[[int], int] means:
# the function takes an int and returns an int.


# Newlines and formatted text

message = "Python\nmakes backend development interesting"

print(message)

formatted = f"```\n{message}\n```"

print(formatted)