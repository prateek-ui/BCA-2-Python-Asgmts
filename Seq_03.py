# Write a program to input the basic salary of the employee and calculate HRA, DA, and gross salary(HRA = 15% of basic salary, DA = 10% of basic salary)
basic=int(input('Enter basic salary: '))
hra,da=basic*0.15,basic*0.10
print(basic+hra+da)