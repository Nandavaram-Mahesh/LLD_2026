import hashlib
# bcrypt
from abc import ABC , abstractmethod

class HashStrategy(ABC):
    @abstractmethod
    def hash(self, password: str): pass


class SHA256Hash(HashStrategy):
    def hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


# class BcryptHash(HashStrategy):
#     def hash(self, password):
#         return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


class PasswordHasher:
    def __init__(self, strategy: HashStrategy):
        self.strategy = strategy

    def create_hash(self, password):
        return self.strategy.hash(password)


# ✅ Usage
hasher = PasswordHasher(SHA256Hash())
print(hasher.create_hash("mypassword"))
