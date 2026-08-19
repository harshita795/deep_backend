def calculate_discount(price, discount):
    discount_amount = price * discount
    final_price = price - discount_amount

    print(f"Price: {price}")
    print(f"Discount: {discount}")
    print(f"Discount amount: {discount_amount}")
    print(f"Final price: {final_price}")

    return final_price


calculate_discount(100, 0.20)