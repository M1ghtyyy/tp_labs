class Target:
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def special_request(self):
        return "Adaptee: Specific behavior."

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.special_request()}"

def client_code(target: Target):
    print(target.request())

if __name__ == "__main__":
    target = Target()
    client_code(target)

    print("\nClient: The Adaptee has a different interface.")
