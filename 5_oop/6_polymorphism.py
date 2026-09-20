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