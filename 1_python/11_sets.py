# Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

fruits = {"orange", "apple", "banana"}
print(type(fruits)) #set
print(fruits)

# Add Values
fruits.add("guava")
print(fruits)

# Remove value
fruits.remove("guava")
print(fruits)

# An empty set
#! Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, we need to use the set() function.
fruits = set()
fruits.add("apple")
print(fruits)

# set Iteration
#! Sets are unordered, so the order of iteration is not guaranteed.
fruits = {"orange", "apple", "banana"}
for fruit in fruits:
  print(fruit)

# Remove duplicates
def remove_duplicates(spells):
# Conversion method
    return list(set(spells))

# Iteration method
    spells_set = set()
    spells_list = []
    for item in spells:
        if item not in spells_set:
            spells_set.add(item)
            spells_list.append(item)
    return spells_list
    
print(remove_duplicates(["add", "just", "add", "good", "bad", "good"]))

# Set substraction
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2
print(set3)

# Count Vowels
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    unique = set()
    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)
    return count, unique

print(count_vowels("Hello, My name is Harshita"))