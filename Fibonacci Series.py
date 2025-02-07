# Fibonacci series program

num_terms = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive integer")
elif num_terms == 1:
    print(f"Fibonacci sequence up to {num_terms}:")
    print(a)
else:
    print(f"Fibonacci sequence up to {num_terms}:")
    while count < num_terms:
        print(a, end=" ")
        nth = a + b
        # Update values
        a = b
        b = nth
        count += 1
