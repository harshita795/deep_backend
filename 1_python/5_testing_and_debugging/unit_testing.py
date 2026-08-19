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