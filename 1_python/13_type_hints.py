# Type hints are a feature in Python that lets you explicitly state what data type a variable, function parameter, or return value should be.

age: int = 25
name: str = "Harshita"
is_student: bool = True
score: float = 95.5

#! While adding a type hint to a variable declaration like:

score: float = 95.5

#! is considered a bit redundant due to type inference, adding type hints to function parameters is not redundant.

# Function parameters type hints
def greet_player(name: str):
  print(f"Welcome, {name}!")

greet_player("Harshita")

# Return type hints
def get_greeting(name: str) -> str:
    return f"Welcome, {name}!"

print(get_greeting("Harshita"))


# List and Set Hints
def get_unique_items(inventory: list[str]) -> set[str]:
  unique_items = set()

  for item in inventory:
    unique_items.add(item)

  return unique_items

print(get_unique_items(["apple", "banana", "apple"]))

# Dictionary type hints
def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0

print(get_item_count({"apple": 3, "banana": 5}, "apple"))

# Tuple hints
def get_fruit_count(count: int) -> tuple[str, int]:
    if count > 10:
        return "Orange", 1
    return "Apple", 3

print(get_fruit_count((8)))

# Nested type hints
fruits: dict[str, list[str]] = {
    "Apple": ["Red", "Healthy"],
    "Orange": ["Orange"],
}

print(fruits)

# Optional Values
def get_prepared_food(has_food: bool) -> str | None:
  if has_food:
    return "Dosa"
  return None

print(get_prepared_food(True))