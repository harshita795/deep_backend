# Python Variables
# Concepts practiced:
# - Variable creation
# - Reassignment
# - Arithmetic
# - Negative numbers
# - Comments
# - Type checking
# - f-strings
# - None
# - Multiple assignment

# Creating a new variable
name = "Harshita"
print(name)

# Reassigning variables
age = 24
print(age)
age = 23
print(age)
age = 22
print(age)

# Arithmetic with variables
one = 1
two = 2
add = one + two
print(add)

# Negative numbers
marks_a = 100
marks_b = -20
total_marks = marks_a + marks_b
print(total_marks)

# Comments
# Single line comment
"""
This is a multiline string.
It can sometimes be used like a block comment,
but Python technically treats it as a string.
"""

# Type checking
age = 24
is_girl = True
print(type(age)) # int
print(type(is_girl)) # bool

# f-strings in python
print(f"I am building my own deep backend developer skills. My name is {name}.")

# None type variable
bad = None
print(bad is None) # True

# # Multiple assignment
good, bad, cool = 5, 0, 4
print(good, bad, cool)




