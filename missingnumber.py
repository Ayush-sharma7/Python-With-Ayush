a = int(input("enter number of elements: "))
l = []
for i in range(a):
    b = int(input("enter number: "))
    l.append(b)
for i in range(a - 1):
    for j in range(a - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
for i in range(a):
    if l[i] != i + 1:
        print(i + 1, " is missing!!")
        break
else:
    print("nothing is missing")
