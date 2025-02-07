l1 = []
n = int(input("Enter the desired length of list: "))

for i in range(n+1):
    e = int(input("Enter the element: "))
    l1.append(e)

print("List before swapping:", l1)

for i in range(0, len(l1) - 1, 2):
    l1[i], l1[i + 1] = l1[i + 1], l1[i]

print("List after swapping:", l1)