hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'), ('0121', 'IT', 'Mark Blick', '67000'),
('0068', 'IT', 'Kahna Larsen', '112000'), ('0234', 'OPS', 'Jim Smith', '54000')]
# For the contents of this list:
# ∗ Mark just reported a name change. Update Mark’s last name to Blick-Hawley.
# ∗ Jim has accepted a new account manager role in another department. Change Jim’s
# department code from OPS to CS and update his salary to 60000.

# Initial HR list
hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]

for Index, record in enumerate(hr_list):
    if record[2] == 'Mark Blick':
        new_name = 'Mark Blick-Hawley'
        hr_list[Index] = (record[0], record[1], new_name, record[3])  
for Index, record in enumerate(hr_list):
    if record[2] == 'Jim Smith':
        hr_list[Index] = (record[0], 'CS', record[2], '60000')  
print(hr_list)

print("Employee# | DeptCode | Name | Salary")
for record in hr_list:
    employee_number = record[0]
    department_code = record[1]
    name = record[2]
    salary = int(record[3])  
    formatted_salary = f"{salary:,}"
    print(f"{employee_number} | {department_code} | {name} | {formatted_salary}")

