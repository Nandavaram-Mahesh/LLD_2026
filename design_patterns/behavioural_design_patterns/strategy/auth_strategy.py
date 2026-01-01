from abc import ABC, abstractmethod
# AbstractStrategy
class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, data): pass

# Concrete Strategies
class PasswordAuth(AuthStrategy):
    def authenticate(self, data):
        return f"Authenticated using username/password: {data['username']}"


class OAuthAuth(AuthStrategy):
    def authenticate(self, data):
        return f"Authenticated via OAuth provider: {data['provider']}"


class APIKeyAuth(AuthStrategy):
    def authenticate(self, data):
        return f"Authenticated via API Key: {data['api_key']}"

# Client/Context
class AuthContext:
    def __init__(self, strategy: AuthStrategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.authenticate(data)


# ✅ Usage
auth = AuthContext(OAuthAuth())
print(auth.execute({"provider": "Google"}))
