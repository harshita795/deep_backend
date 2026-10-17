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

#! Anonymous Functions
# A lambda is a small anonymous function without a name.
# It contains an expression whose result is returned automatically.


add_one = lambda number: number + 1

print(add_one(5))


# Lambdas are useful for short, simple operations.
# They can also be returned from another function.


def create_multiplier(factor: int):
    return lambda number: number * factor


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))
print(triple(5))

#! Higher-Order Functions
# A higher-order function works with other functions as data.
# It can accept a function, return a function, or both.
#
# Here, transform_values() accepts a function and applies it
# to every value in a list.


def square(number: int) -> int:
    return number * number


def transform_values(numbers: list[int], transform) -> list[int]:
    result = []

    for number in numbers:
        result.append(transform(number))

    return result


numbers = [1, 2, 3, 4]

squared_numbers = transform_values(numbers, square)

print(squared_numbers)

#! Map
# map() applies a function to every item in an iterable.
# It returns an iterator, which can be converted to a list when needed.


def double(number: int) -> int:
    return number * 2


numbers = [1, 2, 3, 4]

doubled_numbers = list(map(double, numbers))

print(doubled_numbers)


# map() can also be used with a lambda for a small transformation.

names = ["harshita", "sakshi", "rahul"]

uppercase_names = list(map(lambda name: name.upper(), names))

print(uppercase_names)


# map() returns an iterator rather than a regular list.

mapped_numbers = map(double, numbers)

print(type(mapped_numbers))


# split() separates a string into a list of lines.
# join() combines the lines back into one string.


document = "first line\nsecond line\nthird line"

lines = document.split("\n")
updated_lines = list(map(lambda line: line.upper(), lines))
result = "\n".join(updated_lines)

print(result)

#! Filter
# filter() keeps only the items for which the given function
# returns True.
# It returns an iterator, so convert it to a list when needed.


def is_even(number: int) -> bool:
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(is_even, numbers))

print(even_numbers)


# filter() can also use a lambda for a small condition.

words = ["python", "", "backend", "", "api"]

valid_words = list(filter(lambda word: word != "", words))

print(valid_words)


# Like map(), filter() does not modify the original collection.

#! Reduce
# reduce() repeatedly combines values and produces one final result.
# The first argument is the function used for combining values.


from functools import reduce


def add(total: int, number: int) -> int:
    return total + number


numbers = [10, 20, 30, 40]

total = reduce(add, numbers)

print(total)


# The result of each step becomes the accumulator for the next step.
# add is passed without (), because reduce() calls it for us.

# Zip
# zip() combines items from multiple iterables by position.
# Each pair is returned as a tuple.


names = ["report", "photo", "notes"]
formats = ["pdf", "jpg", "txt"]

paired = list(zip(names, formats))

print(paired)


#! zip() can be combined with filter()
# to keep only pairs that meet a condition.


valid_formats = ["pdf", "txt"]


def is_valid(pair: tuple[str, str]) -> bool:
    return pair[1] in valid_formats


valid_documents = list(filter(is_valid, paired))

print(valid_documents)


# zip() returns an iterator rather than a regular list.

print(type(zip(names, formats)))