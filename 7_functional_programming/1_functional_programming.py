# Functional Programming
#! Functional programming focuses on composing functions
#! that return new values instead of repeatedly changing state.


def add_tax(price: float) -> float:
    return price * 1.18


def format_price(price: float) -> str:
    return f"₹{price:.2f}"


price = 100.0

final_price = add_tax(price)
display_price = format_price(final_price)

print(display_price)

# Each function returns a value that becomes the next function's input.
# The original price remains unchanged.

#! Python supports functional programming concepts,
#! even though it is not a purely functional language.

# split() converts a string into a list of words.
# len() can then be used to count those words.


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


message = "Python is useful for backend development"

print(count_words(message))

# len(text) would count characters,
# while len(text.split()) counts words.


#! Immutable values cannot be changed after they are created.
# Functional programming prefers immutable data because
# it is easier to reason about and avoids unexpected changes.


numbers = (10, 20, 30)

# A tuple cannot be modified in place.
# numbers[0] = 100  # TypeError

# Instead, create a new tuple.
updated_numbers = numbers + (40,)

print(numbers)
print(updated_numbers)


# Tuples vs Lists
# Lists are mutable, while tuples are immutable.

items = ["apple", "banana"]
items.append("orange")

fixed_items = ("apple", "banana")
new_fixed_items = fixed_items + ("orange",)

print(items)
print(fixed_items)
print(new_fixed_items)


#! Functional programming favors returning new values
#! instead of changing the original value.

def add_item(items: tuple[str, ...], item: str) -> tuple[str, ...]:
    return items + (item,)


original_items = ("apple", "banana")
result = add_item(original_items, "orange")

print(original_items)
print(result)

#! Declarative vs Imperative Programming

# Declarative programming focuses on what result we want,
# without describing every step needed to produce it.

# Imperative programming focuses on how to achieve the result,
# by explicitly describing the steps.


#! Declarative
# We describe the desired result.
filtered_numbers = [number for number in [1, 2, 3, 4, 5] if number % 2 == 0]

print(filtered_numbers)


#! Imperative
# We describe the steps used to produce the result.
numbers = [1, 2, 3, 4, 5]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# CSS is declarative: we describe how elements should look,
# while the browser handles the steps required to display them.
#
# Imperative code explicitly tells the program what steps to execute.

#! Declarative calculations
# Built-in functions can express the result more directly
# without manually managing intermediate state.


def get_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


print(get_average([10, 20, 30]))


# sorted() returns a new list instead of modifying the original list.

numbers = [5, 2, 8, 1]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)


# Floor division (//) returns the whole-number result of division.

print(7 // 2)


# A functional approach avoids mutating the input
# and creates new values when needed.


def get_middle_value(numbers: list[int]) -> int | None:
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    middle_index = (len(sorted_numbers) - 1) // 2

    return sorted_numbers[middle_index]


print(get_middle_value([10, 8, 7, 5]))

#! Functions vs Classes
# Functions and classes solve different kinds of problems.
#
# Prefer functions when working mainly with data transformations
# and when state does not need to persist between operations.
#
# Classes are useful when data and behavior belong together
# and an object needs to maintain state over time.
#
# When unsure, starting with functions can keep the code simpler.
# The choice can be changed later as the project grows.

#! Debugging Functional Programming
# Break complex expressions into smaller steps when debugging.
# Intermediate variables make it easier to inspect each transformation.


def format_message(message: str) -> str:
    cleaned = message.strip()
    uppercase = cleaned.upper()
    without_periods = uppercase.replace(".", "")
    result = f"{without_periods}..."

    return result


print(format_message("  hello world.  "))


# String transformations
# strip() removes whitespace from both ends.
# upper() converts all characters to uppercase.
# replace() replaces matching text.


text = "  Python is fun.  "

print(text.strip())
print(text.upper())
print(text.replace(".", ""))

#! Functional vs OOP
# Functional programming and object-oriented programming are different
# styles of organizing and writing code.
#
# Neither style is always better.
# Python supports ideas from both paradigms, so they can be used together.
#
# Encapsulation, abstraction, and polymorphism can be useful in both styles.
# Inheritance is mainly associated with object-oriented programming.
#
# The right approach depends on the problem being solved.
# A good developer should understand both styles and use them appropriately.

#! Statements vs Expressions
# A statement performs an action.
# An expression produces a value.


number = 10  # assignment statement

total = number * 2  # arithmetic expression


# Function calls are also expressions because they produce a value.

length = len("Python")

print(length)


# Even a function without a return statement produces None.

def show_message() -> None:
    print("Hello")


result = show_message()
print(result)


# Functional programming favors expressions because
# they can be combined, reused, and composed more easily.

total = sum([1, 2, 3, 4]) * 2

print(total)

#! Ternary Expressions
# A ternary expression lets us choose between two values
# based on a condition in a single expression.
#
# Syntax:
# value_if_true if condition else value_if_false


def get_status(is_active: bool) -> str:
    return "Active" if is_active else "Inactive"


print(get_status(True))
print(get_status(False))


# Ternaries are useful for simple conditions.
# For complex logic, a normal if/else block is usually easier to read.