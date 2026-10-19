def display_menu():
    print("1. Load grades\n2. Sorted grades\n3. Lowest grade\n4. Highest grade\n5. Average grade\n0. Exit")


def load_grades(path):
    # YOUR CODE HERE
    file = open(path , 'r')
    data = file.readlines()
    grades = []
    for g in data:
        grade =float(g.strip()) 
        grades.append(grade)
    file.close()
    return grades
    


def find_lowest(grades):
    # YOUR CODE HERE
    if len(grades)==0:
        return None
    
    
    # Lowest_grade = grades[0]
    # for i in range(1,len(grades)):
    #     if Lowest_grade > grades[i]:
    #         Lowest_grade = grades[i]
    sorted_grades = sorted(grades)
    Lowest_grade = sorted_grades[0]
    return Lowest_grade



def find_highest(grades):
    # YOUR CODE HERE
    if len(grades)==0:
        return None
    sorted_grades = sorted(grades)
    hight_grade =sorted_grades[len(sorted_grades)-1]
    return hight_grade



def find_average(grades):
    # YOUR CODE HERE
    if len(grades)==0:
            return None

    sum_grades = sum(grades)
    avg_grades = sum_grades /(len(grades))
    return avg_grades


def main():
    grades = []
    choice = ""

    while choice != "0":
        display_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                filename = input("Enter the grade file: ")
                grades = load_grades(filename)
                print("Grades loaded successfully.")

            case "2":
                if grades:
                    print("Sorted grades:")
                    for grade in sorted(grades):
                        print(grade)
                else:
                    print("No grades loaded.")

            case "3":
                if grades:
                    print("Lowest grade:", find_lowest(grades))
                else:
                    print("No grades loaded.")

            case "4":
                if grades:
                    print("Highest grade:", find_highest(grades))
                else:
                    print("No grades loaded.")

            case "5":
                if grades:
                    print(f"Average grade: {find_average(grades):.2f}")
                else:
                    print("No grades loaded.")

            case "0":
                print("Goodbye!")

            case _:
                print("Unknown command")

main() 