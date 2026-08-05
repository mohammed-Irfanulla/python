class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


if __name__ == "__main__":
    car1 = Car("xyz", 123, 2006)
    print(car1.year, car1.model)
