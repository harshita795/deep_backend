# Python Loops
# Concepts practiced:
# - for loops
# - while loops

# For loop
for i in range(1, 10):
  print(i)

# "end" parameter in print function to print on same line.
for i in range(0, 30):
  print(i, end=" ")

# Unpacking range function using *, this also helps printing on the same line.
print("\n", *range(1,8)) # \n moves the output to a new line

# Using variable as end value in range function
end_value = 51

for i in range(1, end_value):
  print(i, end=" ")

print() # used here for new line

#! range() is used to generate sequences of numbers.

# range() also has optional 3rd parameter called "step"
# can also use a negative step to count backwards
for i in range(10, 1, -1):
  print(i, end=" ")

print()

# Finding the sum of numbers using an in-place variable.
def sum_of_nums(start, end):
  total = 0
  for i in range(start, end):
    total += i
  return total

print(sum_of_nums(2, 8))

# Finding the sum of even numbers using step parameter.
def sum_of_evens(end):
  total = 0
  for i in range(0, end, 2):
    total += i
  return total

print(sum_of_evens(8))

# While loop
#! It's a loop that continues while a condition remains True.
# A for loop condition checks if a sequence is finished.
# A while loop condition checks if a state or situation has changed.

count = 0

while count < 5:
  count += 1
  print(count, end=" ")

print()
# counting backward with a while loop
count = 5

while count > 0:
  count -= 1
  print(count, end=" ")

print()


# while loop used in unknown number of repetitions
password = ""

while password != "python123":
    password = input("Enter password: ")


# Continue statement
#! continue skips the remaining code in the current iteration and moves to the next iteration.
for i in range(1, 10):
  if 3 <= i <= 7:
    continue
  print(i, end=" ")

print()

# skipping multiples of 3
counter = 0
for i in range(1, 15):
  counter += 1
  if counter == 3:
    counter = 0
    continue
  print(i, end=" ")

print()

# Printing only after learning 3 concepts at a time.
counter = 0
for i in range(1, 11, 1):
  counter += 1
  if counter < 3:
    continue
  counter = 0
  print(f"I learned {i} concepts.")


# Break statement
#! break immediately exits the loop when a condition is met.

for i in range(10):
  n = f"{i} * {i} = {i * i}"
  print(n)
  if i >= 5:
    break

# Stop searching when the target is found
numbers = [4, 7, 12, 18, 25]
target = 18

for number in numbers:
  if target == number:
    print(f"{target} found.")
    break

# Stop the loop when the limit is reached
count = 0

while True:
  count += 1
  if count == 5:
    break
  print(count, end=" ")

print()