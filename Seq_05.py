# Write a program to input 3 subject marks of a student and calculate its percentage
sum=0
for i in range(3):
    sum+=int(input('Enter marks:'))
print(sum//3)