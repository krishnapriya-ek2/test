# Student Performance Analysis System

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def find_highest(marks):
    return max(marks)

def find_lowest(marks):
    return min(marks)

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = list(map(int, input("Enter marks of 3 subjects: ").split()))

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = get_grade(average)

    students.append({
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    })

# Sort students by name in ascending order (A to Z)
students.sort(key=lambda student: student["name"],reverse=False)

print("\n--- Student Performance ---")

for student in students:
    print("\nName:", student["name"])
    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Highest Mark:", student["highest"])
    print("Lowest Mark:", student["lowest"])
    print("Grade:", student["grade"])