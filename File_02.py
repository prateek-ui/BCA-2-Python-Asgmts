# WAP to read a file and count uppercase and lowercase and digits in the file
f=open("file1.txt","r")
s=f.read()
countLow,countUpp,countDig=0,0,0
for i in s:
    if i.islower():
        countLow+=1
    elif i.isupper():
        countUpp+=1
    elif i.isdigit():
        countDig+=1
print("Lower:",countLow,"Upper:",countUpp,"Digit:",countDig)