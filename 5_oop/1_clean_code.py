# Clean Code
# Function names should clearly describe what the function does.

def calculate_total(numbers):
  total = 0

  for number in numbers:
    total += number

  return total


numbers = [10, 20, 30]
print(calculate_total(numbers))

# Keep the function name, parameters, and logic aligned with what the function does.

def calculate_remaining_balance(balance: int, payment: int) -> int:
  return balance - payment

print(calculate_remaining_balance(1000, 250))

# DRY (Don't Repeat Yourself)
# Avoid writing the same logic multiple times.
# Move repeated logic into a reusable function.

def calculate_total_price(price, quantity):
  return price * quantity


def calculate_order_total(item1_price, item1_quantity, item2_price, item2_quantity):
  first_item_total = calculate_total_price(item1_price, item1_quantity)
  second_item_total = calculate_total_price(item2_price, item2_quantity)

  return first_item_total + second_item_total

print(calculate_order_total(50, 2, 100, 1))

# DRY review
# Repeated logic should be moved into one reusable function.
# Centralizing logic means future changes only need to be made in one place.
# This reduces duplicate code and makes maintenance easier.