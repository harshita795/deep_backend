import math
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


#! Logarithms calculate the power needed to reach a given number.

print(math.log(32, 2))    # 5.0
print(math.log(100, 10))  # 2.0
print(math.log(81, 3))    # 4.0


# Calculate the number of doubling periods needed to reach a target size.

def get_doubling_periods(initial_size: int, target_size: int) -> float:
    if initial_size <= 0 or target_size <= 0:
        raise ValueError("Sizes must be positive")

    if target_size < initial_size:
        raise ValueError("Target size must not be smaller than initial size")

    return math.log(target_size / initial_size, 2)


print(get_doubling_periods(10, 80))    # 3.0
print(get_doubling_periods(25, 100))   # 2.0


# Calculate a score using the logarithm of a user's activity count.

def calculate_activity_score(activity_count: int, engagement_rate: float) -> float:
    if activity_count <= 0:
        return 0.0

    return engagement_rate * math.log(activity_count, 2)


print(calculate_activity_score(64, 5.0))  # 30.0
print(calculate_activity_score(0, 5.0))   # 0.0
