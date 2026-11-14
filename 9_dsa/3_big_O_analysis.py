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
