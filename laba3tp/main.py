from abc import ABC, abstractmethod

###########################################################################################################################################################
################################################################ SINGLETON ################################################################################
###########################################################################################################################################################

class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("use get_instance()")
        print('singleton is live')

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance


    def some_method(self):
        pass



singleton = Singleton.get_instance()
singleton.some_method()

# second_instance = Singleton()  # <- exception

###########################################################################################################################################################
################################################################ FACTORY METHOD ###########################################################################
###########################################################################################################################################################

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class FileLogger(Logger):
    def log(self, message: str):
        print(f"\nLogging to file: {message}")


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Logging to console: {message}")



class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass


    def log_message(self, message: str):
        logger = self.create_logger()
        logger.log(message)


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


if __name__ == "__main__":
    file_logger_factory = FileLoggerFactory()
    file_logger_factory.log_message("message")

    console_logger_factory = ConsoleLoggerFactory()
    console_logger_factory.log_message("message")


###########################################################################################################################################################
################################################################ ABSTRACT FACTORY #########################################################################
###########################################################################################################################################################


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print("Windows button")


class MacButton(Button):
    def paint(self):
        print("Mac button")


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows checkbox")


class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

if __name__ == "__main__":
    print("\nWindows:")
    windows_app = Application(WindowsFactory())
    windows_app.paint()

    print("\nMac:")
    mac_app = Application(MacFactory())
    mac_app.paint()


###########################################################################################################################################################
################################################################ BUILDER ##################################################################################
###########################################################################################################################################################


# Продукт
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def __str__(self):
        return f"Pizza(dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}')"


class PizzaBuilder:
    def build_dough(self):
        pass

    def build_sauce(self):
        pass

    def build_topping(self):
        pass

    def get_result(self) -> Pizza:
        pass


class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")

    def build_sauce(self):
        self.pizza.set_sauce("mild")

    def build_topping(self):
        self.pizza.set_topping("ham+pineapple")

    def get_result(self) -> Pizza:
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


if __name__ == "__main__":
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    director.construct_pizza()
    pizza = builder.get_result()

    print(pizza)

#                                                                    OUTPUT


#       singleton is live

#       Logging to file: message
#       Logging to console: message

#       Windows:
#       Windows button
#       Windows checkbox
#
#       Mac:
#       Mac button
#       Mac checkbox