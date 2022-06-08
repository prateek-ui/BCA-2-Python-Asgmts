# WAP to read a file and display the longest word present in a file
f=open("file1.txt","r")
s1=f.read().split()
max=0
s2=""
for i in s1:
    if max<len(i):
        max=len(i)
        s2=i
print(s2)