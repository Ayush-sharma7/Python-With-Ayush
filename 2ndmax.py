# secondlargest
l = []
a = int(input("enter number of elements: "))
for i in range(a):
    b = int(input("enter number: "))
    l.append(b)
max = l[0]
for i in range(1, a):
    if max < l[i]:
        max = l[i]
max2 = l[0]
for i in range(1, a):
    if max2 < l[i] and l[i] != max:
        max2 = l[i]
print(max2)
