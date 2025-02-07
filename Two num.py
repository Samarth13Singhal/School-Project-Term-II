a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"{a} is greater than {b} by {a-b}")

elif b > a:
    print(f"{b} is greater than {a} by {b-a}")

else:
    print("Both numbers are equal")