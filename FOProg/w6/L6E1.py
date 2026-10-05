# Lecture 6 Example 1

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start_engine(self):
        print(self.brand + " says WROOM!")


# Lets create two cars
car1 = Car("Tesla", "Black", 2019)
car2 = Car("Skoda", "Grey", 2012)

# Get the brand
print("car1 is of brand", car1.brand)
print("car2 is of brand", car2.brand)

# Start the engines!!
car1.start_engine()
car2.start_engine()
