# You have to calculate an employee's salary by computing the gross salary tax and net salary based on the given parameters.

Base_Salary = 50000
Bonus = 5000
Tax_Rate = 10
Other_Charges = 2000
print("The Base Salary of Employee is:",Base_Salary)
print("The Bonus of the Employee:",Bonus)
print("The Tax Rate on income is :",Tax_Rate)
print("Other charges on income are:",Other_Charges)
gross_salary=Base_Salary+Bonus-Other_Charges
print("The Gross Salary of the Employee is:",gross_salary)
e=gross_salary*10/100
print("The tax on salary is:",e)
f=gross_salary-e
print("The net salry of the Employee after tax deduction is:",f)
