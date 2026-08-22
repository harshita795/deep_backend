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

# Modulo operator %
# Find the odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = []
for number in numbers:
  if number % 2 != 0:
    odd_numbers.append(number)
print(odd_numbers)

# Slicing Lists
#! List slicing returns a new list from the existing list.
scores = [50, 70, 30, 20, 90, 10, 50]
print(scores[1:5:2])

# Omitting Sections
print(scores[:3])
print(scores[3:])

# Using only the step section
print(scores[::2])

# Negative Indices
#! Negative indices count from the end of the list.
print(scores[-3:])
print(scores[-2:])
print(scores[-1:]) #gives the last item in the list
print(scores[-6:-3])
print(scores[-3:-6])  #[]

# Slicing the items list
items = ["apple", "banana", "orange", "apple", "banana", "guava"]
print(items[2:]) # from 3rd fruit to last
print(items[:-1]) # from start to end, except last fruit
print(items[::2]) # from start to end even positions, 0 is even.

# List concatenation
list_A = [1,2,3] 
list_B = [4,5,6]
print(list_A + list_B)

# List Conatins
items = ["apple", "banana", "orange", "guava"]
print("apple" in items)
print("apple" not in items)
print("mango" not in items)

# List Deletion
def del_items(items):
  del items[0]
  del items[-2:]
  # return is not needed here, because the deletion happens in memory.
del_items(items)
print(items)

# list in-place modification done by .append(), .pop(), del

# Tuples are collections of data that are ordered and unchangeable. We can think of a tuple as a List with a fixed size.
my_tuple = ("this is a toy", 45, True)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Single item tuple
my_name = ("Harshita",) # We must include a comma so Python knows it's a tuple and not regular parentheses

# Tuple Unpacking
my_info = ("Harshita", 24, True)
name, age, is_good = my_info
print(name)
print(age)
print(is_good)

#! When we return multiple values from a function, we're actually returning a tuple.

# List of tuples
my_info = [
  (
    "Harshita",
    24,
    True
  ),
  (
    "Harsh",
    17,
    True
  ),
  (
    "Harshit",
    28,
    False
  )
]

print(my_info[0])
print(my_info[1])
print(my_info[2])
print(my_info[0][0])
print(my_info[1][0])
print(my_info[2][0])

# Returning first element
def firstElement(items):
  if len(items) == 0:
    return "ERROR"
  return items[0]

print(firstElement([1, 2]))
print(firstElement([]))


# Reverse list
def reverse_list(items):
  new_items = []

  for i in range(len(items)-1, -1, -1):
    new_items.append(items[i])
  return new_items

print(reverse_list([1,2,400,6,3]))

# Reverse list using slice
items = [1,2,400,6,3]
print(items[::-1])

# Split a string into list of words
my_string = "My name is Harshita"
print(my_string.split())

# Join a List of Strings Into a Single String
my_list = ["My", "name", "is", "Harshita"]
print(" ".join(my_list))

# Filter messages
def filter_messages(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
          words = message.split()
          good_words = []
          dang_counter = 0
          for word in words:
            print(word)
            if word == "dang":
                dang_counter += 1
            else:
                good_words.append(word)
          joined = " ".join(good_words)
          filtered_messages.append(joined)
          words_removed.append(dang_counter)
    return filtered_messages, words_removed
                
 
    
print(filter_messages([ "I enjoy learning Python", "this dang error is difficult to fix", "lets build a backend project"]))

# slice odd even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"even_numbers: {numbers[1::2]}")
print(f"odd_numbers: {numbers[::2]}")


# Matching between lists
def check_ingredient_match(recipe, inventory):
  missing_ingredients = []
  for item in recipe:
    if item not in inventory:
      missing_ingredients.append(item)
       
  percentage = 100 - (len(missing_ingredients) / len(recipe) * 100)
  return percentage, missing_ingredients

print(check_ingredient_match(["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"],  ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]))