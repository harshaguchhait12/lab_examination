"""
Question 4: Employee Salary Analysis 
A company stores employee salaries in a list. Write a function to 
calculate the average salary, display salaries above the average, 
and increase every salary by 10%. 
"""


emp_sal=[50000,60000,70000,80000, 90000,80000]

def sal_analysis(salary):
    average_salary=sum(salary) / len(salary)
    salary_above_avg=[i for i in salary if i > average_salary]
    updated_salary=[i+i*(10/100) for i in salary]
    return{
        "average_salary": average_salary,
        "salary_above_average": salary_above_avg,
        "updated_salary": updated_salary
    }

result=sal_analysis(emp_sal)
print(result)