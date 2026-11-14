# O(n): The number of operations grows with the input size.

def find_max_response_time(response_times: list[float]) -> float:
    if not response_times:
        raise ValueError("Response times cannot be empty")

    highest_time = response_times[0]

    for time in response_times:
        if time > highest_time:
            highest_time = time

    return highest_time


print(find_max_response_time([120.5, 85.2, 240.8, 150.0]))  # 240.8


#! O(n²): Nested loops compare every element with every other element.

def find_matching_products(
    first_list: list[int],
    second_list: list[int]
) -> list[int]:
    matches = []

    for product_one in first_list:
        for product_two in second_list:
            if product_one == product_two and product_one not in matches:
                matches.append(product_one)

    return matches


print(find_matching_products([101, 202, 303], [202, 404, 101]))  # [101, 202]
