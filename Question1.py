"""
Question 1: Student Marks Analysis 
A college stores students' marks in a list. Write a function that 
accepts a list of marks and displays the highest mark, lowest 
mark, average mark, and number of students who passed (marks 
of 40 or above). 

"""

marks = [90, 85, 79, 97, 86,33,15]

def mark_i(marks):
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / len(marks)

    passed_students = 0
    for mark in marks:
        if mark >= 40:
            passed_students += 1

    Failed_students = 0
    for mark in marks:
            if mark < 40:
                Failed_students += 1

    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Students Passed: {passed_students}")
    print(f"Students Failed: {Failed_students}")
    
mark_i(marks)