from collections.abc import Callable
from functools import lru_cache

def track_response_status(
    func: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, dict[int, int]]]:
    status_counts: dict[int, int] = {}

    def wrapper(
        endpoint: str, status_code: int
    ) -> tuple[str, dict[int, int]]:
        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        response = func(endpoint, status_code)
        return response, status_counts.copy()

    return wrapper


@track_response_status
def build_response(endpoint: str, status_code: int) -> str:
    return f"Endpoint: {endpoint}, Status: {status_code}"


print(build_response("/users", 200))
print(build_response("/users", 200))
print(build_response("/candidates", 404))


#! *args collects positional arguments into a tuple.
# **kwargs collects keyword arguments into a dictionary.

def args_logger(*args: object, **kwargs: object) -> None:
    # Print positional arguments with numbers starting from 1.
    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")

    # Sort keyword arguments alphabetically by key.
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")


args_logger("GET", "/users", status_code=200, duration_ms=45)

# Why *args and **kwargs?
# They allow functions to accept a variable number of arguments.


#! A decorator can modify arguments before passing them to a function.
def trim_text_arguments(
    func: Callable[..., str],
) -> Callable[..., str]:
    def wrapper(*args: str, **kwargs: str) -> str:
        # Remove extra spaces from positional and keyword values.
        clean_args = tuple(arg.strip() for arg in args)
        clean_kwargs = {key: value.strip() for key, value in kwargs.items()}

        # Pass the cleaned arguments to the original function.
        return func(*clean_args, **clean_kwargs)

    return wrapper


@trim_text_arguments
def format_message(title: str, message: str) -> str:
    return f"{title}: {message}"


print(format_message("  Alert  ", message="  Server is running  "))
# Alert: Server is running


# Why transform arguments in a decorator?
# It lets us apply common input-cleaning logic to multiple functions
# without repeating that logic inside each function.


#! Cache results to avoid recomputing the same inputs.
@lru_cache
def is_palindrome(word: str) -> bool:
    # A word with 0 or 1 characters is a palindrome.
    if len(word) <= 1:
        return True

    # If the outer characters differ, it isn't a palindrome.
    if word[0] != word[-1]:
        return False

    # Check the remaining characters recursively.
    return is_palindrome(word[1:-1])


print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))   # False
print(is_palindrome("level"))    # True


#! Why LRU Cache?
# @lru_cache stores results for previously used inputs.
# LRU means Least Recently Used; older cache entries may be
# removed when the cache reaches its size limit.
#
#! Recursion
# A function calls itself with a smaller input until it
# reaches a base case.