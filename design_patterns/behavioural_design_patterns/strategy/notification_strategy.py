from abc import ABC , abstractmethod
class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, msg): pass


class EmailNotification(NotificationStrategy):
    def send(self, msg):
        print(f"Email sent: {msg}")


class SMSNotification(NotificationStrategy):
    def send(self, msg):
        print(f"SMS sent: {msg}")


class PushNotification(NotificationStrategy):
    def send(self, msg):
        print(f"Push Notification: {msg}")


class Notifier:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notify(self, msg):
        self.strategy.send(msg)


# ✅ Usage
notifier = Notifier(PushNotification())
notifier.notify("Your order has been shipped!")
