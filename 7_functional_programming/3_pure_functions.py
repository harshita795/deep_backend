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


#! Properties of Pure functions
# Pure functions are deterministic:
# the same inputs always produce the same output.
#
# They do not:
# - modify external state
# - depend on variables outside their scope
# - perform I/O such as file, network, or console operations
#
# Avoiding side effects makes pure functions easier to test,
# debug, and reason about.


#! Reference vs Value
# Mutable objects can be changed through a reference.
# Immutable values cannot be changed in place.


# Lists are mutable.

def add_number(numbers: list[int]) -> None:
    numbers.append(4)


numbers = [1, 2, 3]

add_number(numbers)

print(numbers)
# [1, 2, 3, 4]


# Integers are immutable.

def increase_number(number: int) -> None:
    number += 1


value = 10

increase_number(value)

print(value)
# 10


# Avoid mutating a dictionary passed into a function.
# Create a copy and return the updated dictionary.


def enable_format(settings: dict[str, bool], format_name: str) -> dict[str, bool]:
    new_settings = settings.copy()
    new_settings[format_name] = True

    return new_settings


settings = {
    "pdf": True,
    "docx": False,
}

updated_settings = enable_format(settings, "txt")

print(settings)
print(updated_settings)

# The original dictionary stays unchanged.

#! Pass-by-Reference Impurity
# Mutable objects can be changed inside a function through a reference.
# This can accidentally create side effects and make a function impure.


def add_tag(tags: list[str], tag: str) -> None:
    tags.append(tag)


tags = ["python"]

add_tag(tags, "backend")

print(tags)
# ["python", "backend"]


# A safer approach is to create a new list instead of modifying the input.

def add_tag_safely(tags: list[str], tag: str) -> list[str]:
    new_tags = tags.copy()
    new_tags.append(tag)

    return new_tags


original_tags = ["python"]
updated_tags = add_tag_safely(original_tags, "backend")

print(original_tags)
print(updated_tags)

#! Input and Output
# I/O means interacting with the outside world.
# Examples include printing, files, databases, and network requests.
#
# I/O is a side effect, so pure functions should avoid it.


def convert_case(text: str, case: str) -> str:
    if case == "upper":
        return text.upper()

    if case == "lower":
        return text.lower()

    if case == "title":
        return text.title()

    raise ValueError("unsupported case")


text = "python backend development"

print(convert_case(text, "upper"))
print(convert_case(text, "title"))


# The function returns a value instead of printing it.
# This keeps the transformation separate from the I/O.


#! Containing I/O
# I/O is necessary, but it is better to keep it separate
# from the main data-processing logic.
#
# A common structure is:
#
#   input → pure processing → output
#
# For example, reading and writing a file can be handled
# outside, while the data in between is processed by pure functions.


def count_words(text: str) -> int:
    return len(text.split())


text = "Python is useful for backend development"

word_count = count_words(text)

print(word_count)

#! No-Op
# A no-op is an operation that produces no useful result
# and does not cause a side effect.


def unused_calculation(number: int) -> None:
    number * 2


# Printing is an I/O operation, so it is a side effect.

def show_name(name: str) -> None:
    print(name)


# A pure version returns the value instead.

def format_name(name: str) -> str:
    return name.upper()


print(format_name("harshita"))


# Avoid changing global state inside a function.
# Pass the data in and return a new value instead.

def remove_emphasis(text: str) -> str:
    words = text.split()
    clean_words = map(lambda word: word.strip("*"), words)

    return " ".join(clean_words)


document = "*Python* is **great**"

clean_document = remove_emphasis(document)

print(clean_document)

# The original document is unchanged.