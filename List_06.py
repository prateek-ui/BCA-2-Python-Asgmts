# WAP to count the number of strings where the string length is 2 or more and the first and last characters are same from a given list of strings
ls=[ "abc", "g", "xyz", "aba", "121"]
count=0
for i in ls:
    if len(i)>2 and i[0]==i[len(i)-1]:
        count+=1
print(count)