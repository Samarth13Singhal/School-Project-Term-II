a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("First number is largest")
elif a < b and b > c:
    print("Second number is largest")
elif a < c and b < c:
    print("Third number is largest")
elif a == b and a > c:
    print("Third number is smallest")
elif a == c and a > b:
    print("Second number is smallest")
elif c == b and a < c:
    print("First number is smallest")
else:
    print("All numbers are equal")