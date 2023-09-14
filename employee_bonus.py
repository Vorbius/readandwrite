import csv

employees= open ('EmployeePay.csv','r')

csv_file= csv.reader(employees)
next(csv_file)

for record in csv_file:
    total= int(record[3])*float(record[4])+int(record[3])
    bonus=float(record[4])*int(record[3])
    print(f'First Name: {record[1]} \nLast Name: {record[2]} \nSalary: ${float(record[3]):1,.2f} \nBonus: ${bonus:10,.2f} \nTotal: ${total:10,.2f}')
    input()
employees.close()