# Program to count and display vowels, consonants, uppercase, and lowercase in a string

input_string = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0
uppercase_count = 0
lowercase_count = 0

# Define sets of vowels
vowels = 'aeiouAEIOU'

# Iterate through each character in the string
for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
        
        if char.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1

# Display the results
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
