# Week 10 - Example 2

cars = [
    {"brand": "Ford", "year": 2015, "price": 15000},
    {"brand": "Skoda", "year": 2012, "price": 5000}
]

for car in cars:
    if car["brand"] == "Ford":
        print("Year of the Ford is:", car["year"])
