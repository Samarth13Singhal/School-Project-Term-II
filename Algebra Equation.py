from math import factorial

welcome = 'Welcome to the Series Calculator'
print(welcome.center(50,'.'))

print('\n\nIt has the following Series:-')

print("\nSeries 1: 1 + x + x\u00b2+ x\u00b3 +......+ x\u1D51")
print("Series 2: 1 - x + x\u00b2 - x\u00b3 +......+ x\u1D51")
print("Series 3: 1 + x\u00b2/2 + x\u00b3/3 +......+ x\u1D51/\u006E")
print("Series 4: 1 + x\u00b2/2! + x\u00b3/3! +......+ x\u1D51/\u006E!\n")

series = int(input("Enter 1-4 to select the series: "))

#Variables and Constants
x = int(input("\nEnter the value of x: "))
n = int(input("Enter the length of the series, n: "))
result = 0

# Series 1
if series == 1:

    for i in range(n+1):
        if i == 0:
            result += 1
        elif i == 1:
            result += x
        else:
            result += x**i
    print(f"\nThe result of series is: {result}")

# Series 2
elif series == 2:
    
    for i in range(n+1):
        if i == 0:
            result += 1
        elif i % 2 != 0:
            result -= x**i
        else:
            result += x**i
    print(f"\nThe result of series is: {result}")

elif series == 3:

    for i in range(1, n+1):
        if i == 0:
            result += 1
        else:
            result += (x**i)/i
    print(f"\nThe result of series is: {result}")

elif series == 4:
    
    for i in range(1, n+1):
        if i == 0:
            result += 1
        else:
            result += (x**i)/factorial(i)
    print(f"\nThe result of series is: {result}")

else:
    print("\nInvalid selection. The series is not available.\n Please try again...")
