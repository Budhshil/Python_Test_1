# Employee sorted arry

def sort_employees_by_id(employees):
    # Sort employees by 'id' in ascending order
    sorted_employees = sorted(employees, key=lambda x: x['id'])
    return sorted_employees

def sort_employees_by_salary(employees):
    # Sort employees by 'salary' in descending order
    sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)
    return sorted_employees

emp = [
    {"id": 101, "name": "John", "salary": 60000},
    {"id": 103, "name": "Alice", "salary": 75000},
    {"id": 102, "name": "Bob", "salary": 65000},
    ]
#print(sort_employees_by_id(emp))

# After calling sor_employee_id:
# o/p : [{'id': 101, 'name': 'John', 'salary': 60000}, {'id': 102, 'name': 'Bob', 'salary': 65000}, {'id': 103, 'name': 'Alice', 'salary': 75000}]

print(sort_employees_by_salary(emp))
# After Calling Sort_employee_by_salary:
#O/p : [{'id': 103, 'name': 'Alice', 'salary': 75000}, {'id': 102, 'name': 'Bob', 'salary': 65000}, {'id': 101, 'name': 'John', 'salary': 60000}]


