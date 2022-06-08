# Accept email-address from user and display its username with the help of slicing operator
str=input("Enter email address: ")
print(str[:str.index('@')])
