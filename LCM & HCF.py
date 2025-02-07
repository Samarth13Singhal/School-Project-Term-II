n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

fact_n = []
fact_m = []
c_fact = []

for i in range(1,n+1):
    if n % i == 0:
        fact_n.append(i)

for i in range(1,m+1):
    if m % i == 0:
        fact_m.append(i)

for e in fact_n:
    if e in fact_m:
        c_fact.append(e)

Hcf = max(c_fact)
Lcm = (n*m) // Hcf

print("HCF and LCM of the given numbers are", Hcf, "and", Lcm," respectively")


# Find HCF using the Euclidean algorithm
# a = 48
# b = 18

# while b:
#     a, b = b, a % b

# print("HCF:", a)
