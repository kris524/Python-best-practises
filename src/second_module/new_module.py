


class Something:
    name = "jack" #class attribute

    def __init__(self, ball, dog):
        self.ball = ball
        self.dog = dog #instance attribute

    @staticmethod
    def nature():
        print("we are in a forest") # cannot access neither instance nor class attributes

    @classmethod
    def print_name(cls): #needs the cls infront
        print(cls.name) #can only access the class attributes

    @classmethod
    def factory_method(cls): #you can make factory methods with this
        #you can use it to make classes with
        return cls("tenis", "terri")


if __name__ == "__main__":
    std = Something.factory_method()
    print(std.ball)
    print(std.dog)