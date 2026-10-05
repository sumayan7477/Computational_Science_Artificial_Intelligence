# Lecture 6 Example 2

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country
    
    def is_adult(self):
        return self.age >= 18       

    def update_age(self, new_age):
        self.age = new_age

    def update_country(self, new_country):
        self.country = new_country

 
# Creating an instance of the Person class
person1 = Person("Alice", 30, "USA")
person2 = Person("Pekka", 17, "Finland")

# Person 1 introduction
print("Hi, I am " + person1.get_name() + "!")
print("I am " + str(person1.get_age()) + " years old.")
print("I live in " + person1.get_country() + ".\n")

# Person 1 moves to Canada
person1.update_country("Canada")
print("Now I live in " + person1.get_country() + ".\n")

##################3

# Person 2 introduction
print("Hi, I am " + person2.get_name() + "!")
print("I am " + str(person2.get_age()) + " years old.")
print("I live in " + person2.get_country() + ".\n")

# Let define a simple function

def can_by_alcohol(human):
    if human.is_adult():
        print(human.get_name() + " can buy alcohol in Finland")
    else:
        print(human.get_name() + " cannot buy alcohol in Finland")

can_by_alcohol(person2)

# Person 2 turns 18
person2.update_age(18)

# What is the situation now?
can_by_alcohol(person2)






