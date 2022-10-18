


class Something:
    name = "jack" #class attribute

    def __init__(self, ball):
        self.ball = ball
        self.dog = dog #instance attribute

    @staticmethod
    def nature():
        print("we are in a forest") # cannot access neither instance nor class attributes

    @classmethod
    def print_name(cls): #needs the cls infront
        print(cls.name) #can only access the class attributes

    @classmethod
    def factory_method(cls):
        #you can use it to make classes with
        return cls("Steve")