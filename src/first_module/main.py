"""The Factory method defines a method that is used to create other objects, 
the Subclasses will override the method to change the class of objects that will be created"""

from abc import ABC, abstractmethod

class Main(ABC):
    
    @abstractmethod
    def factory_method(self):
        """the subclasses of the Main class will create other classes using this method"""
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class Product(ABC):

    @abstractmethod
    def operation(self)-> str:
        pass


# These are the specific Factories, they return a abstract Product in general so they stay independent
#DONT FORGET, we overwrote the factory method, but we still have some_operation()
class SpecificProductCreator1(Main):
    def factory_method(self) -> Product:
        return SpecificProduct1()

class SpecificProductCreator2(Main):
    def factory_method(self) -> Product:
        return SpecificProduct2()


# These are the specific Products
class SpecificProduct1(Product):
    def operation(self) -> str:
        return "This is Specific Product 1"


class SpecificProduct2(Product):
    def operation(self) -> str:
        return "This is Specific Product 2"


def client_code(creator: Main) -> None:
    print(f"The Creator currently in use is: {creator.some_operation()}")


if __name__ == "__main__":
    print("For SpecificProductCreator1")
    client_code(SpecificProductCreator1())

    print("For SpecificProductCreator2")
    client_code(SpecificProductCreator2())
