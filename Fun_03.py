# Make a function which will take a string and return the count of vowels and consonants present in that string
def isVowel(c):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    return False
def countVow(str):
    count=0
    for i in str:
        if isVowel(i)==True:
            count+=1
    return count
str=input("Enter string: ")
print("Count of vowel:", countVow(str.lower()),"Count of consonants:", len(str)-countVow(str.lower()))