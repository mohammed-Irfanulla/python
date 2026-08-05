class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


if __name__ == "__main__":
    dog1 = Dog("Buddy", 3)
    print(dog1.name)
    print(dog1.species)

    dog2 = Dog("Bulldog", 1)
    print(dog2.name)
    print(dog2.species)
    print(dog1, dog2)
