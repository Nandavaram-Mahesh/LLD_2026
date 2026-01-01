from abc import ABC,abstractmethod

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, data): pass


class FileStorage(StorageStrategy):
    def save(self, data):
        print("Saving to file:", data)


class SQLStorage(StorageStrategy):
    def save(self, data):
        print("Saving to SQL database:", data)


class MongoStorage(StorageStrategy):
    def save(self, data):
        print("Saving to MongoDB:", data)


class DataSaver:
    def __init__(self, strategy: StorageStrategy):
        self.strategy = strategy

    def save_data(self, data):
        self.strategy.save(data)


# ✅ Usage
saver = DataSaver(MongoStorage())
saver.save_data({"user": "Alice"})
