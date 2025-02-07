str1 = input("Enter a word: ")
str2 = str1.lower()

if str2 == str2[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")