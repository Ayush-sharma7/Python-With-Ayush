l = []
a = int(input("enter no. of elements:"))
for i in range(0, a):
    b = int(input("enter value:"))
    l.append(b)
x = []
for i in l:
    if i not in x:
        x.append(i)
for i in x:
    y = 0
    for j in l:
        if i == j:
            y += 1
    print("frequency of", i, "is:", y)
