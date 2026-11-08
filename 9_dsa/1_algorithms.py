
# An algorithm is a finite sequence of steps used to solve a problem.

def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))

def find_minimum(nums: list[int]) -> int | None:
    if not nums:
        return None

    minimum = float("inf")

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum

print(find_minimum([8, 3, 12, 1, 6]))

def summed(nums: list[int]) -> int:
    total = 0

    for num in nums:
        total += num

    return total

print(summed([2, 4, 6, 8]))

def get_first_item(nums: list[int]) -> int | None:
    if not nums:
        return None

    return nums[0]

print(get_first_item([10, 20, 30]))

def print_items(nums: list[int]) -> None:
    for num in nums:
        print(num)

print_items([1, 2, 3])
