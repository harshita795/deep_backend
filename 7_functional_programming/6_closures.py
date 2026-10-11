from collections.abc import Callable

# A closure remembers variables from the scope where
# the inner function was created, even after the outer
# function has returned.


def create_counter(start: int = 0) -> Callable[[], int]:
    count = start

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3


# Each call updates the same remembered variable.
# nonlocal allows the inner function to modify
# the variable in the enclosing function's scope.


another_counter = create_counter(10)

print(another_counter())  # 11
print(another_counter())  # 12

# Each closure maintains its own independent state.

# Closures can maintain state between calls.
# When they modify that state, they are not pure functions
# because successive calls can produce different results.