# Abstraction focuses on exposing essential features while hiding complexity
# Encapsulation focuses on bundling data with methods and restricting direct access to implementation details

# In other words..
# Abstraction
# Abstraction hides unnecessary implementation details
# and gives the user a simple interface to work with.
#
# Encapsulation protects internal state,
# while abstraction focuses on what the object exposes.


class EmailService:
    def __init__(self, address: str) -> None:
        self.__address = address

    def send(self, message: str) -> None:
        self.__connect()
        print(f"Sending '{message}' to {self.__address}")

    def __connect(self) -> None:
        print("Connecting to mail server...")


service = EmailService("harshita@example.com")

service.send("Hello!")

# The implementation behind the interface can change
# without changing how the caller uses the class.
#
# Abstraction is about reducing complexity for the user of the class.