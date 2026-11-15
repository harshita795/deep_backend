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


#! O(n * m): Two nested loops process two different input sizes.

def calculate_average_sales(store_sales: list[list[int]]) -> float:
    total_sales = 0
    total_stores = len(store_sales)

    if not store_sales:
        return 0.0

    for sales in store_sales:
        for quantity in sales:
            total_sales += quantity

    return total_sales / total_stores


print(calculate_average_sales([
    [10, 20, 30],
    [15, 25],
    [40, 50, 60]
]))  #  # 83.3333333333333


#! O(1): Dictionary lookup takes constant time on average.

def find_employee_department(
    employees: dict[int, str],
    employee_id: int
) -> str | None:
    if employee_id not in employees:
        return None

    return employees[employee_id]


employee_departments = {
    101: "Engineering",
    102: "Marketing",
    103: "Finance"
}

print(find_employee_department(employee_departments, 102))


#! O(log n): Binary search on a sorted list.

def find_product_price(prices: list[int], target: int) -> bool:
    low = 0
    high = len(prices) - 1

    while low <= high:
        middle = (low + high) // 2

        if prices[middle] == target:
            return True
        elif prices[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return False


product_prices = [100, 250, 400, 550, 700, 850, 1000]

print(find_product_price(product_prices, 550))
