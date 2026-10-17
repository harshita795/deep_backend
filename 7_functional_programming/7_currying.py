from collections.abc import Callable

# Currying transforms a multi-argument function into
# nested functions that each accept a single argument.


# Normal function: accepts two arguments.
def add(a: int, b: int) -> int:
    return a + b


print(add(3, 5))  # 8


# Curried function: accepts one argument at a time.
def curried_add(a: int) -> Callable[[int], int]:
    def add_b(b: int) -> int:
        return a + b

    return add_b


print(curried_add(3)(5))  # 8


# The returned function can be saved and reused.
add_ten = curried_add(10)

print(add_ten(2))  # 12
print(add_ten(7))  # 17


# eg - calculate font sizes for different document types.
def convert_font_size(font_size: int) -> Callable[[str], int]:
    def convert(doc_type: str) -> int:
        multipliers = {"txt": 1, "md": 2, "docx": 3}

        if doc_type not in multipliers:
            raise ValueError("unsupported document type")

        return font_size * multipliers[doc_type]

    return convert


font_converter = convert_font_size(12)

print(font_converter("txt"))   # 12
print(font_converter("md"))    # 24
print(font_converter("docx"))  # 36

#! Why Currying?
# Currying can adapt a function to match an expected signature.
# For example, a library may expect a function that accepts
# one argument, while our original function needs multiple arguments.
#
# We can supply one argument in advance and return a function
# that accepts the remaining argument.