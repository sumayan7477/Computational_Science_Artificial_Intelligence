"""
From the web page of Kiasma museum https://kiasma.fi/en/visitor-information/
we see that the opening hours are:

Tue: 10–20
Wed–Thu: 10–18
Fri: 10–20
Sat–Sun: 10–17
Mon: Closed

We write a program that tells the opening hours of a given day.
"""

day = input("Give a day (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ")

match day:
    case "Mon":
        print("Closed")
    case "Tue" | "Fri":
        print("Open 10-20")
    case "Wed" | "Thu":
        print("Open 10-18")
    case "Sat" | "Sun":
        print("Open 10-17")
    case _:
        print("There is no such day")
