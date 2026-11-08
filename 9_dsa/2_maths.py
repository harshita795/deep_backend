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
