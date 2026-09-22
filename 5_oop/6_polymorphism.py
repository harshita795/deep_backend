# Polymorphism
# Different objects can provide the same method with different behavior.
# The caller can use the same method name without caring about the object's type.


class EmailNotification:
    def send(self):
        print("Sending email")


class SMSNotification:
    def send(self):
        print("Sending SMS")


class PushNotification:
    def send(self):
        print("Sending push notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

for notification in notifications:
    notification.send()

#! Duck typing
# Python cares about whether an object supports the required behavior,
# rather than requiring it to be a specific type.

#! Function / Method Signatures
# A function signature describes the function name and its parameters.
# Using the same signature across different implementations allows
# different objects to be used through the same interface.
#
# The return type annotation documents the expected output,
# but Python does not use it to distinguish functions.


# Same interface, different implementations
class PDFReport:
    def generate(self, title: str) -> str:
        return f"PDF: {title}"


class HTMLReport:
    def generate(self, title: str) -> str:
        return f"HTML: {title}"


reports = [PDFReport(), HTMLReport()]

for report in reports:
    print(report.generate("Monthly Report"))


# Operator Overloading
# Special methods can define how built-in operators work with custom objects.
# The + operator calls the __add__ method.


class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            raise TypeError("can only add Money objects")

        return Money(self.amount + other.amount)


cash_one = Money(500)
cash_two = Money(300)

total = cash_one + cash_two

print(total.amount)

#! cash_one + cash_two is translated to cash_one.__add__(cash_two)


# Overriding Built-in Methods
# Dunder methods let us customize how Python handles our objects.
#
# __str__ is used for a readable representation of an object.
# __repr__ is mainly used for debugging and development.


class Task:
    def __init__(self, title: str, completed: bool) -> None:
        self.title = title
        self.completed = completed

    def __str__(self) -> str:
        return f"{self.title} - completed: {self.completed}"

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, completed={self.completed!r})"


task = Task("Learn Python", True)

print(task)
print(repr(task))