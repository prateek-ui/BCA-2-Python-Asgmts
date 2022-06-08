# Accept a string from the user and find the count of uppercase and lowercase letters and digits
str=input("Enter string: ")
countLow=0
for i in str:
    if i.islower():
        countLow+=1
print("Count of lower: %i, Count of upper: %i" %(countLow, len(str)-countLow))