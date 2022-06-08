# Make a function which will take a string and find the maximum occurring character
def maxChar(str):
    max=0
    ch=''
    for i in str:
        if max<str.count(i):
            max=str.count(i)
            ch=i
    return ch
print(maxChar(input("Enter string: ")))