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


# These are the specific Factoties, they return a abstract product in general so they stay indep
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



