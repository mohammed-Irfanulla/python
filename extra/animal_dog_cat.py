class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)


class Dog(Animal):
    def sound(self):
        print(self.name, "barks")


class Cat(Animal):
    def sound(self):
        print(self.name, "meow")


if __name__ == "__main__":
    d = Dog("Buddy")
    d.info()
    d.sound()

    d2 = Cat("Kitty")
    d2.info()
    d2.sound()
