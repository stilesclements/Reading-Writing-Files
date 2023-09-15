import csv

EmployeePay=open("EmployeePay.csv","r")
Pay_csv=csv.reader(EmployeePay)

next(Pay_csv)

for rec in Pay_csv:
    Salary=float(rec[3])
    Bonus_per=float(rec[4])
    Bonus=Salary*Bonus_per
    Total_sal=Salary+Bonus
    print(f"ID: {rec[0]}\nFirst Name: {rec[1]}\nLast Name: {rec[2]}\nSalary: ${Salary:10,.2F}\nBonus: ${Bonus:10,.2F}\nTotal Salary: ${Total_sal:10,.2F}")
    input()

    #ID,EmpFName,EmpLName,Salary,Bonus