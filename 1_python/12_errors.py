# Errors and Exceptions in Python

# There are two main kinds of errors:
# - Syntax errors
# - Exceptions


# Syntax Error
# A syntax error occurs when code does not follow Python's syntax rules.

# Example: Missing a colon at the end of an if statement
# if amount > 10
#     print("Too high!")


# Exception
# An exception occurs when the code has valid syntax,
# but an unexpected problem happens while the program is running.

# Example: The syntax is valid, but division by zero raises an exception.
# result = 10 / 0


# Raising and handling an exception
# get_player_record() raises an exception when a player ID is not found.
# main() catches and handles that exception.

def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
        print(get_player_record(5))
    except Exception as e:
        print(e)


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    if player_id == 5:
        return {"name": "Gandalf", "level": 5000}

    raise Exception("player id not found")


main()


# Errors vs Bugs
# Exceptions can occur because of unexpected runtime situations
# and may need to be handled.
# Bugs are problems in the program's logic that need to be fixed.


# Error Raising vs Handling
# Raising an exception signals that a problem has occurred.
# Handling an exception allows the program to respond to that problem.

# Handling a specific exception: ZeroDivisionError
try:
    10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e)


# Handling an IndexError when accessing an invalid list index
try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("Index out of range")
except Exception as e:
    print(e)


# Manually raising and catching a specific exception
try:
    raise ZeroDivisionError("zero division")
except ZeroDivisionError as e:
    print("zero")


# Handling different exception types
# The specific exception is checked before the general Exception.
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")


# Catching any exception using the general Exception class
try:
    10 / 0
except Exception as e:
    print("other")