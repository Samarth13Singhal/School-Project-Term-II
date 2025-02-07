#List
l1 = []
j = int(input("Enter the desired length of list: "))

for i in range(j):
    n = int(input("Enter the number: "))
    l1.append(n)

print("Maximum in List:", max(l1))
print("Minimum in List:", min(l1))

#Tuple 
t1 = ()
m = int(input("Enter the desired length of tuple: "))

for i in range(m):
    n = int(input("Enter the number: "))
    t1 += (n,)

print("Maximum in Tuple:", max(t1))
print("Minimum in Tuple:", min(t1))
