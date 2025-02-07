n = int(input("Enter the number: "))
factors = []

for i in range(1, n+1):
    if n % i == 0:
        factors.append(i)

print(f"The factors of {n} are: {factors}")
if len(factors) == 2:
    print("It is a prime number")
elif len(factors) > 2:
    print("It is a composite number")