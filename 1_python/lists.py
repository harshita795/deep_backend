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