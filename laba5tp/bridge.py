class Implementation:
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB"

class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: {self.implementation.operation_implementation()}"

class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"ExtendedAbstraction: {self.implementation.operation_implementation()}"

def client_code(abstraction: Abstraction):
    print(abstraction.operation())

if __name__ == "__main__":
    implementation_a = ConcreteImplementationA()
    abstraction = Abstraction(implementation_a)
    client_code(abstraction)

    implementation_b = ConcreteImplementationB()
    extended_abstraction = ExtendedAbstraction(implementation_b)
    client_code(extended_abstraction)
