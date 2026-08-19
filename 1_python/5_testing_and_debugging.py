# Python Testing and Debugging
# Concepts practiced:
# - Unit testing
# - Debugging
# - Stack traces


# Unit testing
def calculate_total(price, quantity):
    return price * quantity


def test_calculate_total():
  test_cases = [
    (10, 2, 20),
    (25, 4, 100),
    (5, 0, 0),
    ]

  for price, quantity, expected in test_cases:
    result = calculate_total(price, quantity)

    if result == expected:
      print(f"PASS: {price} × {quantity} = {result}")
    else:
      print(f"FAIL: expected {expected}, got {result}")


test_calculate_total()


# Debugging
def calculate_discount(price, discount):
  discount_amount = price * discount
  final_price = price - discount_amount

  print(f"Price: {price}")
  print(f"Discount: {discount}")
  print(f"Discount amount: {discount_amount}")
  print(f"Final price: {final_price}")

  return final_price


calculate_discount(100, 0.20)


# Stack traces
def calculate_average(total, count):
  return total / count


def process_scores():
  total = 100
  count = 0

  return calculate_average(total, count)


# This intentionally raises ZeroDivisionError
# so the Python stack trace can be examined.
process_scores()