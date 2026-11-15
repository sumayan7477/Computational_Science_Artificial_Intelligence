import csv

def load_grades(filename):
    data=[]
    csvfile = open(filename, "r")
    reader = csv.DictReader(csvfile)

    for row in reader:
        row["score"] = float(row["score"])
        data.append(row)
    csvfile.close()
    return data

def student_grades(data):
    students = {}

    for row in data:
        name = row["name"]
        score = row["score"]

        if name in students:
            students[name].append(score)
        else:
            students[name]=[score]
    return students

def student_average(grades):
    if len(grades)==0:
        return 0.0
    else:
        total = 0

        for grade in grades:
            total = total + grade
        return total/len(grades)

def best_student(students):
    if len(students) == 0:
        return None
    else:
        best_name = None
        highest_average = 0

        for name in students:
            average = student_average(students[name])

            if best_name is None or average > highest_average:
                highest_average = average
                best_name = name
        return best_name

def main():
    data = load_grades("grades.csv")

    for row in data:
         print(row)

    students = student_grades(data)

    print("\nStudent grades:")
    for name, grades in students.items():
        print(f"{name}:{grades} (Avg: {student_average(grades):.2f})")

    best = best_student(students)
    print(f"\n Best student: {best}")

#main()



















        
