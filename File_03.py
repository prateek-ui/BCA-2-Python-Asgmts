# WAP to accept input from user and check if that input is present in file or not, if present then how many times and if not then display proper message
f=open("file1.txt","r")
s1=f.read()
s2=input("Input: ")
if s2 in s1:
    print(s1.count(s2))
else:
    print("Input not present")