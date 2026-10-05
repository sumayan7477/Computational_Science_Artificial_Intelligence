# Lecture 6 Example 2

class Person:
    def __init__(self, name, age, country):
        self.age = age
        self.name = name
        self.country = country

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country

    def is_adult(self):
        return self.age >= 18

    def update_age(self, age):
        self.age = age

    def update_country(self, country):
        self.country = country

person1 = Person("Alice", 30, "USA")
person2 = Person("Pekka", 17, "Finland")

print("Hi, I am " + person1.get_name() + "!")
print("I am  " + str(person1.get_age()) + " years old")
print("I live in " + person1.get_country())

person1.update_country("Canada")
print("Now, I live in " + person1.get_country())

print(person2.get_name() + " is an adult? " + str(person2.is_adult()))
person2.update_age(18)
print(person2.get_name() + " is an adult? " + str(person2.is_adult()))
