# Accept a string from user and reverse every word at its own place
str=input("Enter string: ")
str1=str.split(' ')
str=""
for i in str1:
    str+=i[::-1]
    str+=' '
print(str.strip())