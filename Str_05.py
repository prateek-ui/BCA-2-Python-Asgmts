# Accept a string and remove all duplicate characters
str=input("Enter string: ")
for i in str:
    c=str.count(i)
    if c>1:
        str=str.replace(i,'')
print(str)