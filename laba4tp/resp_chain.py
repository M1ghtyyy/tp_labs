from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class AuthenticationHandler(AbstractHandler):
    def handle(self, request):
        if not request.get("authenticated", False):
            print("Authentication failed.")
            return "Stop"
        print("Authentication passed.")
        return super().handle(request)

class AuthorizationHandler(AbstractHandler):
    def handle(self, request):
        if request.get("role") != "admin":
            print("Authorization failed.")
            return "Stop"
        print("Authorization passed.")
        return super().handle(request)

class LoggingHandler(AbstractHandler):
    def handle(self, request):
        print(f"Logging request: {request}")
        return super().handle(request)

if __name__ == "__main__":
    auth_handler = AuthenticationHandler()
    authz_handler = AuthorizationHandler()
    log_handler = LoggingHandler()

    auth_handler.set_next(authz_handler).set_next(log_handler)

    request = {"authenticated": True, "role": "admin", "data": "some_data"}
    print(auth_handler.handle(request))

    request = {"authenticated": False, "role": "user", "data": "some_data"}
    print(auth_handler.handle(request))
