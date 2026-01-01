from abc import ABC , abstractmethod

class LoggerStrategy(ABC):
    @abstractmethod
    def log(self, message): pass


class ConsoleLogger(LoggerStrategy):
    def log(self, message):
        print(f"[Console]: {message}")


class FileLogger(LoggerStrategy):
    def log(self, message):
        with open("app.log", "a") as f:
            f.write(message + "\n")


class RemoteLogger(LoggerStrategy):
    def log(self, message):
        print(f"[Remote Log]: Sending '{message}' to server...")


class AppLogger:
    def __init__(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def log(self, message):
        self.strategy.log(message)


# ✅ Usage
logger = AppLogger(FileLogger())
logger.log("Server started at port 8080")
