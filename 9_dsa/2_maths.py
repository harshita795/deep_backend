# Exponents: Raising a number to a power using **.

square = 4 ** 2
cube = 3 ** 3
power = 2 ** 5

print(square)  # 16
print(cube)    # 27
print(power)   # 32


# Calculate estimated content reach using average audience size and exponential growth.

def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0

    total = 0

    for followers in audiences_followers:
        total += followers

    average_followers = total / len(audiences_followers)
    estimated_spread = average_followers * (len(audiences_followers) ** 1.2)

    return estimated_spread


print(get_estimated_spread([10, 20, 30]))
print(get_estimated_spread([5, 15, 25, 35]))
print(get_estimated_spread([]))


#! Geometric progression: Each term is calculated by multiplying the previous term by a constant.

def calculate_savings_growth(
    initial_amount: int,
    monthly_multiplier: int,
    num_months: int
) -> int:
    return initial_amount * (monthly_multiplier ** num_months)


print(calculate_savings_growth(100, 2, 3))  # 800
print(calculate_savings_growth(500, 3, 2))  # 4500
print(calculate_savings_growth(200, 2, 0))  # 200


# Predict growth based on a category.

def get_growth_prediction(
    initial_value: int,
    growth_type: str,
    num_months: int
) -> int:
    if growth_type == "fast":
        multiplier = 4
    elif growth_type == "medium":
        multiplier = 3
    else:
        multiplier = 2

    return initial_value * (multiplier ** num_months)


print(get_growth_prediction(10, "fast", 2))    # 160
print(get_growth_prediction(10, "medium", 2))  # 90
print(get_growth_prediction(10, "slow", 2))    # 40

