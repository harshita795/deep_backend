# Python Lists

# A list stores multiple values in a single variable.
languages = ["Python", "JavaScript", "Java"]
print(languages)

# Accessing a specific item using its index
languages = ["Python", "JavaScript", "Java", "Go"]
item_index = 1
print(languages[item_index])

# Getting the length of a list
languages = ["Python", "JavaScript", "Java", "Go"]
print(len(languages))

# Finding the last index of a list
last_index = len(languages) - 1
print(last_index)

# Updating a list item
languages = ["Python", "JavaScript", "Java", "Go"]
if languages[2] == "Java":
  languages[2] = "C#"

print(languages)

# Appending items to a list adds an element to the end of the list
numbers = []

for i in range(1, 6):
  numbers.append(i)

print(numbers)

# Pop removes the last element from a list 
#! .pop() is the opposite of .append(). 

# Removing items from a list using pop()
languages = ["Python", "JavaScript", "Go", "Rust"]
last_language = languages.pop()

print(last_language)
print(languages)

# Removing an item at a specific index
numbers = [10, 20, 30, 40, 50]
removed_number = numbers.pop(2)

print(removed_number)
print(numbers)

# Counting the items in a list

apple_count = 0
orange_count = 0
banana_count = 0

items = ["apple", "banana", "orange", "apple", "banana"]
for i in range(0, len(items)):
  if items[i] == "apple":
    apple_count += 1
  elif items[i] == "banana":
    banana_count += 1
  elif items[i] == "orange":
    orange_count +=1

print(f"apple_count: {apple_count}, orange_count: {orange_count}, banana_count: {banana_count}")

# Find an item in a list
# no-index syntax
found = False

for item in items:
  if item == "orange": 
    found = True
print(found)

# Find the increase
old_ages = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
new_ages = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

for i in range(0, len(old_ages)):
  if old_ages[i] < new_ages[i]:
    print(i, end=" ")

print()

# Find Max
nums = [1,4,5,8,2,3]
max_so_far = float("-inf")
for num in nums:
  if num > max_so_far:
    max_so_far = num
print(max_so_far)
        