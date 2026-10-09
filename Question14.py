"""
Question 14: Student Result Management 
A college stores student names and marks in a dictionary. Write a 
function that displays each student's result, calculates the class 
average, and identifies students who scored at least 75 marks. 
def student_results(students): 

"""
def student_results(students):
    total = 0

    for name, marks in students.items():
        print(f"{name}: {marks} marks")
        total += marks

    average = total / len(students)
    print(f"Class Average: {average}")

    print("Students scoring 75 or above:")

    for name, marks in students.items():
        if marks >= 75:
            print(f"{name}: {marks}")


student_results({
    "Tufan": 85,
    "Harsha": 92,
    "Samprit": 67,
    "Samnath": 78,
    "Anuvab": 55
})