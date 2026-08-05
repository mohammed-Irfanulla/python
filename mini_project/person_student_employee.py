class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks


class Employee(Person):
    def __init__(self, name, age, exp, sal):
        super().__init__(name, age)
        self.exp = exp
        self.sal = sal


if __name__ == "__main__":
    employee1 = Employee("Irfan", 20, 2, 20000)
    print(employee1.name, employee1.sal)
