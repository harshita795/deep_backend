# Python Computing
# Concepts practiced:
# - Arithmetic operators
# - In-place operators
# - Scientific notation
# - Logical operators
# - Binary numbers
# - Bitwise operators
# - Binary conversion


# Arithmetic operators
first_number = 20
second_number = 6

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
remainder = first_number % second_number
power = first_number ** 2

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(floor_division)
print(remainder)
print(power)


# In-place operators
score = 100

score += 20
print(score)

score -= 10
print(score)

score *= 2
print(score)

score /= 2
print(score)


# Scientific notation
large_number = 3.5e10
small_number = 4.5e-4

print(large_number)
print(small_number)


# Logical operators
is_logged_in = True
has_access = True

can_access_dashboard = is_logged_in and has_access
print(can_access_dashboard)

is_admin = False
is_manager = True

has_management_access = is_admin or is_manager
print(has_management_access)


# Not operator
is_blocked = False

can_continue = not is_blocked
print(can_continue)


# Binary numbers
binary_number = 0b1010

print(binary_number)


# Bitwise AND
first_permission = 0b1100
second_permission = 0b1010

shared_permissions = first_permission & second_permission

print(shared_permissions)


# Bitwise OR
first_permission = 0b0101
second_permission = 0b0011

combined_permissions = first_permission | second_permission

print(combined_permissions)


# Converting binary strings
binary_value = "10101"

decimal_value = int(binary_value, 2)

print(decimal_value)