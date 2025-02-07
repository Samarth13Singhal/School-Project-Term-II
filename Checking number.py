n = int(input("Enter the number: "))

# Checking a Prefect number
sum_of_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
is_perfect = sum_of_divisors == n

# Checking a Armstrong number
str_n = str(n)
len_n = len(str_n)
sum_of_numbers = 0
for digit in str_n:
    sum_of_numbers += int(digit) ** len_n
is_armstrong = sum_of_numbers == n

# Checking palindrome
is_palindrome = str_n == str_n[::-1].lower()

# Printing the result
if is_palindrome:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")

if is_perfect:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

if is_armstrong:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")


