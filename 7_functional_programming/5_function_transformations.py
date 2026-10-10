from collections.abc import Callable


# Function Transformations
# A function can accept another function and return a new function.
# The returned function uses the behavior of the function it received.


def colon_formatter(first: str, second: str) -> str:
    return f"{first}: {second}"


def create_logger(
    formatter: Callable[[str, str], str]
) -> Callable[[str, str], None]:

    def logger(first: str, second: str) -> None:
        print(formatter(first, second))

    return logger


# Create a new function using the colon formatter.
info_logger = create_logger(colon_formatter)

info_logger("API", "Request received")
info_logger("Database", "Connection established")


# A different formatter creates a different logger.

def dash_formatter(first: str, second: str) -> str:
    return f"{first} - {second}"


debug_logger = create_logger(dash_formatter)

debug_logger("Worker", "Job completed")

#! Why Transform?
# Function transformations let us reuse common logic
# while creating functions with different behavior.


def make_formatter(prefix: str, suffix: str) -> Callable[[str], str]:
    def format_text(text: str) -> str:
        return f"{prefix}{text}{suffix}"

    return format_text


# Create specialized functions from the same implementation.

bold = make_formatter("**", "**")
italic = make_formatter("*", "*")
bullet = make_formatter("* ", "")

print(bold("Python"))
print(italic("Python"))
print(bullet("Python"))
