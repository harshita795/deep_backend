# Encapsulation
# Encapsulation means keeping an object's internal data and implementation details
# controlled inside the class.
#
# Public members can be accessed directly from outside the class.
# Private members are intended to be used only inside the class and are prefixed
# with two underscores (__).
#
# Python does not enforce private members like some other languages.
# Instead, double underscores trigger name mangling, which changes the attribute
# name internally to make direct access less straightforward.


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name          # public attribute
        self.__age = age          # private attribute

    def get_age(self) -> int:
        return self.__age

    def update_age(self, age: int) -> None:
        self.__age = age


user = User("Harshita", 24)

# Public attribute can be accessed directly.
print(user.name)

# Private data should be accessed through public methods.
print(user.get_age())

user.update_age(25)
print(user.get_age())


# Name mangling
# Python internally changes __age to _User__age.
# This is why direct access using user.__age does not work normally.

# print(user.__age)   # AttributeError

# Name mangling can still be accessed using the internally changed name.
# This shows that Python's private members are not truly private.
print(f"Name mangling: {user._User__age}")

#! Encapsulation is about organization, not security.

# Private members are used to mark internal implementation details.
# They are not meant to provide true security or secrecy.
# The goal is to hide unnecessary implementation details and make a class
# easier to use and maintain.


# Encapsulation in practice

class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        self.__owner = owner
        self.__balance = balance

    def get_owner(self) -> str:
        return self.__owner

    def get_balance(self) -> float:
        return self.__balance

    def add_money(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")

        self.__balance += amount

    def spend_money(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")

        if amount > self.__balance:
            raise ValueError("insufficient balance")

        self.__balance -= amount


wallet = Wallet("Harshita", 500)

print(wallet.get_owner())
wallet.add_money(200)
wallet.spend_money(150)

print(wallet.get_balance())