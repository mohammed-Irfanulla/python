class Father:
    def __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage


class Mother:
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage


class Child(Father, Mother):
    def __init__(self, fname, fage, mname, mage, name, age):
        Father.__init__(self, fname, fage)
        Mother.__init__(self, mname, mage)
        self.name = name
        self.age = age

    def info(self):
        print(self.fname, self.mname, self.name)


if __name__ == "__main__":
    child1 = Child("Raj", 12, "Raji", 12, "Rajesh", 10)
    child1.info()
