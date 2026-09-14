# Python Functions
# Concepts practiced:
# - Function definition
# - Parameters
# - Arguments
# - Return values
# - Multiple parameters
# - Default parameters
# - Multiple return values
# - Function execution order


# Basic function
def greet_user(name):
    return f"Hello, {name}!"


print(greet_user("Harshita"))


# Function with multiple parameters
def calculate_salary(monthly_salary, bonus): # Parameters
    return monthly_salary + bonus


total_salary = calculate_salary(50000, 5000) # Arguments
print(f"Total salary: {total_salary}")


# Function with a default parameter
def create_profile(name, role="Backend Developer"):
    return f"{name} - {role}"


print(create_profile("Harshita"))
print(create_profile("Harshita", "Integration Engineer"))


# Multiple return values
def calculate_api_stats(successful, failed):
    total = successful + failed
    success_rate = (successful / total) * 100

    return total, success_rate


total_requests, success_rate = calculate_api_stats(95, 5)

print(f"Total requests: {total_requests}")
print(f"Success rate: {success_rate}%")