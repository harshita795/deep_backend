# Pure Functions
# A pure function:
# - returns the same result for the same inputs
# - does not change data outside its own scope
#
# Pure functions are easier to test, debug, and reason about.


def calculate_discount(price: float, discount: float) -> float:
    return price - (price * discount)


print(calculate_discount(100, 0.10))
print(calculate_discount(100, 0.10))


# Impure functions depend on or modify external state.

total = 0


def add_to_total(amount: int) -> None:
    global total
    total += amount


add_to_total(100)
print(total)


# The pure function depends only on its inputs.
# The impure function changes data outside its own scope.
#
# Prefer pure functions when practical because they
# produce predictable results without side effects.


# Properties of Pure functions
#! Pure functions are deterministic:
# the same inputs always produce the same output.
#
#! They do not:
# - modify external state
# - depend on variables outside their scope
# - perform I/O such as file, network, or console operations
#
#! Avoiding side effects makes pure functions easier to test,
# debug, and reason about.

