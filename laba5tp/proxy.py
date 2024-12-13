class Subject:
    def request(self):
        raise NotImplementedError("You should implement this method.")

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()
        else:
            print("Proxy: Access denied.")

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to real request.")
        return True

    def log_access(self):
        print("Proxy: Logging")

def client_code(subject: Subject):
    subject.request()

if __name__ == "__main__":
    print("code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nclient code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
"""

                    OUTPUT 

                    
code with a real subject:
RealSubject: Handling request.

client code with a proxy:
Proxy: Checking access prior to real request.
RealSubject: Handling request.
Proxy: Logging


"""