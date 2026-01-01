from abc import ABC, abstractmethod

class CacheStrategy(ABC):
    @abstractmethod
    def get(self, key): pass

    @abstractmethod
    def set(self, key, value): pass


class InMemoryCache(CacheStrategy):
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


class RedisCache(CacheStrategy):
    def get(self, key):
        print(f"Fetching {key} from Redis")

    def set(self, key, value):
        print(f"Setting {key}:{value} in Redis")


class FileCache(CacheStrategy):
    def get(self, key):
        print(f"Reading {key} from cache.txt")

    def set(self, key, value):
        print(f"Writing {key}:{value} to cache.txt")


class CacheContext:
    def __init__(self, strategy: CacheStrategy):
        self.strategy = strategy

    def cache_data(self, key, value):
        self.strategy.set(key, value)

    def retrieve_data(self, key):
        return self.strategy.get(key)


# ✅ Usage
cache = CacheContext(InMemoryCache())
cache.cache_data("token", "xyz123")
