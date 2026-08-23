# Dictionaries in Python are used to store data values in key -> value pairs.
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2019,
}

# Setting dictionary values
full_names = ["Harshita Yadav", "Saurabh Rabta"]

names_dict = {}
for full_name in full_names:
  name_parts = full_name.split()
  names_dict[name_parts[0]] = name_parts[1]

print(names_dict)

# Deleting dictionary values
del names_dict["Harshita"]
print(names_dict)

# Counting the same key and putting in value
def count_fruits(fruit_names):
  fruits_dict = {}
  for fruit_name in fruit_names:
    if fruit_name in fruits_dict:
      fruits_dict[fruit_name] += 1
    else:
      fruits_dict[fruit_name] = 1
  return fruits_dict

print(count_fruits(["orange", "banana", "apple", "orange"]))

# Iterating over dictionary
def get_most_common_fruit(fruits_dict):
  max_so_far = float("-inf")
  most_common_fruit = None
  for fruit_name in fruits_dict:
    if fruits_dict[fruit_name] > max_so_far:
      max_so_far = fruits_dict[fruit_name]
      most_common_fruit = fruit_name
  return most_common_fruit
            
print(get_most_common_fruit({"orange": 3, "banana": 2, "apple": 6, "guava": 8}))

#! As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries were unordered.

# Getting Fruit colour
def fruit_color(fruit_data):
  return fruit_data["fruits"]["apple"]["color"]

fruit_data = {
    "fruits": {
        "orange": {
            "count": 3,
            "color": "orange"
        },
        "banana": {
            "count": 2,
            "color": "yellow"
        },
        "apple": {
            "count": 6,
            "color": "red"
        },
        "guava": {
            "count": 8,
            "color": "green"
        }
    }
}

print(fruit_color(fruit_data))

# Merge dictionaries
#! Dictionaries cannot contain duplicate keys.
def merge(dict1, dict2):
  merge_dict = {}
  for key in dict1:
    merge_dict[key] = dict1[key]
  for key in dict2:
    merge_dict[key] = dict2[key]
  return merge_dict

dict1 = {"apple": 2, "orange": 1}
dict2 = {"banana": 4, "apple": 5}
print(merge(dict1, dict2))