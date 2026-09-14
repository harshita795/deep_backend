# Python Comparisons and Conditional Logic
# Concepts practiced:
# - Comparison operators
# - Boolean values
# - Comparison evaluation
# - if statements
# - if/else statements
# - if/elif/else statements
# - Boolean logic
# - and
# - or
# - not
# - Chained comparisons
# - Conditional decision making


# Comparison operators
# <  less than
# >  greater than
# <= less than or equal to
# >= greater than or equal to
# == equal to
# != not equal to

first_number = 10
second_number = 20

print(first_number < second_number)   # True
print(first_number > second_number)   # False
print(first_number <= second_number)  # True
print(first_number >= second_number)  # False
print(first_number == second_number)  # False
print(first_number != second_number)  # True


# Comparison results are boolean values

age = 25
minimum_age = 18

is_old_enough = age >= minimum_age
print(is_old_enough)  # True


# Comparing values and storing the result

python_score = 85
database_score = 72

python_is_higher = python_score > database_score
database_is_higher = database_score > python_score
scores_are_equal = python_score == database_score

print(python_is_higher)
print(database_is_higher)
print(scores_are_equal)


# Comparing multiple values

height_a = 160
height_b = 160
height_c = 155

is_a_b_same = height_a == height_b
is_a_c_same = height_a == height_c
is_b_c_same = height_b == height_c

print(is_a_b_same)
print(is_a_c_same)
print(is_b_c_same)


# Comparison practice with variables

available_memory = 8
required_memory = 4

has_enough_memory = available_memory >= required_memory
print(has_enough_memory)  # True


# if statement
# Code inside the if block runs only when the condition is True

logged_in = True

if logged_in:
  print("User is logged in")


# if statement with a comparison

temperature = 30

if temperature > 25:
  print("It is a warm day")


# if statement with a return value

def check_password_length(password):
  if len(password) >= 8:
    return "password length is valid"

  return "password is too short"


print(check_password_length("python123"))
print(check_password_length("hello"))


# if/else statement

balance = 500

if balance >= 100:
  print("Purchase can be completed")
else:
  print("Insufficient balance")


# if/else with equality

current_role = "backend"

if current_role == "backend":
  print("Working on backend development")
else:
  print("Working on another area")


# if/elif/else statement

score = 78

if score >= 90:
  result = "excellent"
elif score >= 70:
  result = "good"
elif score >= 50:
  result = "average"
else:
  result = "needs improvement"

print(result)


# Multiple conditions using and
# Both conditions must be True

age = 25
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)  # True


# Multiple conditions using or
# At least one condition must be True

is_weekend = False
is_holiday = True

can_take_break = is_weekend or is_holiday
print(can_take_break)  # True


# Using not
# not reverses a boolean value

is_busy = False

can_start_task = not is_busy
print(can_start_task)  # True


# Combining and, or, and not

age = 25
has_account = True
is_blocked = False

can_access = age >= 18 and has_account and not is_blocked
print(can_access)  # True


# Chained comparisons

hour = 7

is_working_hours = 5 <= hour <= 10
print(is_working_hours)  # True


# Another chained comparison example

score = 85

is_valid_score = 0 <= score <= 100
print(is_valid_score)  # True


# Function using comparison operators

def compare_numbers(number_a, number_b):
  if number_a > number_b:
    return "first number is greater"
  elif number_a < number_b:
    return "second number is greater"
  else:
    return "both numbers are equal"


print(compare_numbers(20, 10))
print(compare_numbers(10, 20))
print(compare_numbers(10, 10))


# Function using >=

def can_handle_task(experience_years, required_years):
  return experience_years >= required_years


print(can_handle_task(2, 1))  # True
print(can_handle_task(1, 3))  # False


# Equality check with if/else

def check_username(username, expected_username):
  if username == expected_username:
    return "username matches"
  else:
    return "username does not match"


print(check_username("harshita", "harshita"))
print(check_username("harshita", "developer"))


# if/elif/else based on a value

def classify_age(age):
  if age < 13:
    return "child"
  elif age < 18:
    return "teenager"
  else:
    return "adult"


print(classify_age(10))
print(classify_age(16))
print(classify_age(25))


# Boolean logic in a practical example

def can_apply_for_job(experience_years, knows_python, has_degree):
  return experience_years >= 1 and knows_python and has_degree


print(can_apply_for_job(2, True, True))
print(can_apply_for_job(0, True, True))


# Using or in a practical example

def can_use_learning_resource(has_internet, has_downloaded_copy):
  return has_internet or has_downloaded_copy


print(can_use_learning_resource(True, False))
print(can_use_learning_resource(False, True))
print(can_use_learning_resource(False, False))


# Combining conditions inside if/elif/else

def evaluate_candidate(experience_years, knows_python, knows_apis):
  if experience_years >= 2 and knows_python and knows_apis:
    return "strong match"
  elif knows_python or knows_apis:
    return "potential match"
  else:
    return "needs more preparation"


print(evaluate_candidate(2, True, True))
print(evaluate_candidate(0, True, False))
print(evaluate_candidate(0, False, False))


# Boolean expression evaluation

number = 15

is_positive = number > 0
is_even = number % 2 == 0
is_in_range = 1 <= number <= 20

print(is_positive)
print(is_even)
print(is_in_range)


# Combining comparison results

age = 25
has_experience = True
has_required_skill = True

eligible = (
    age >= 18
    and has_experience
    and has_required_skill
)

print(eligible)


# conditional decision making

def decide_next_step(score, completed_project):
  if score >= 80 and completed_project:
    return "ready for the next level"
  elif score >= 60 or completed_project:
    return "continue practicing"
  else:
    return "review the fundamentals"


print(decide_next_step(90, True))
print(decide_next_step(65, False))
print(decide_next_step(40, False))