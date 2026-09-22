# Classes
# A class defines a custom type with related data and behavior.
# An object is an instance created from a class.


class Student:
    name: str = "Harshita"
    age: int = 24
    is_learning: bool = True


# Creating an object (instance) from the class
student = Student()

print(student.name)
print(student.age)
print(student.is_learning)

# Methods
# A method is a function defined inside a class.
# It can access and modify the object's data through self.


class BankAccount:
    balance: int = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount


account = BankAccount()

account.deposit(500)
print(account.balance)

# self refers to the object that called the method.
# Different objects can have their own state.

first_account = BankAccount()
second_account = BankAccount()

first_account.deposit(1000)
second_account.deposit(300)

print(first_account.balance)
print(second_account.balance)

# Methods can return values
# A method can use an object's properties to calculate and return a value.


class Product:
    price: int = 100
    quantity: int = 2

    def get_total_price(self) -> int:
        return self.price * self.quantity


product = Product()

print(product.get_total_price())

#! Methods vs Functions

# A method is a function that is defined inside a class
# and is used to work with the data of an object.

# Functions are called directly, while methods are called through an object.

# OOP groups related data and behavior together.
# Methods can modify an object's state without necessarily returning a value.

# OOP and functional programming are different programming styles.
# Understanding both approaches helps in choosing the right one for a problem.

# Constructors
# __init__ is a special method that runs automatically
# when a new object is created.
# It lets us set instance properties when the object is initialized.


class User:
    def __init__(self, name: str, age: int, role: str) -> None:
        self.name = name
        self.age = age
        self.role = role


user_one = User("Harshita", 24, "Backend Developer")
user_two = User("Saurabh", 27, "Software Engineer")

print(user_one.name)
print(user_one.age)
print(user_one.role)

print(user_two.name)
print(user_two.age)
print(user_two.role)

# Multiple Objects
# A class can be used to create multiple objects.
# Each object is a separate instance with its own data.


class Employee:
    def __init__(self, name: str, role: str, salary: int) -> None:
        self.name = name
        self.role = role
        self.salary = salary


employee_one = Employee("Harshita", "Backend Developer", 60000)
employee_two = Employee("Sakshi", "Software Engineer", 75000)

print(employee_one.name, employee_one.role, employee_one.salary)
print(employee_two.name, employee_two.role, employee_two.salary)

# Class Variables vs Instance Variables
# Instance variables belong to a specific object.
# Class variables are shared by all objects of the class.


class User:
    role = "Developer"  # class variable

    def __init__(self, name: str) -> None:
        self.name = name  # instance variable


user_one = User("Harshita")
user_two = User("Sakshi")

print(user_one.name)
print(user_two.name)
print(user_one.role)
print(user_two.role)

# Changing an instance variable affects only that object.

user_one.name = "Harshita Yadav"

print(user_one.name)
print(user_two.name)

# Changing the class variable affects objects that use the class attribute.

User.role = "Engineer"

print(user_one.role)
print(user_two.role)