l = []
a = int(input("enter number of elements: "))
for i in range(a):
    b = int(input("enter number: "))
    l.append(b)
for i in range(a - 1):
    for j in range(a - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)
