# Make a function which will take a string and check whether it is palindrome or not
def palindrome(str):
    if str == str[::-1]:
        return True
    return False
print(palindrome(input("Enter string: ")))