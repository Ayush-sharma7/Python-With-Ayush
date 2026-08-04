a, b = 0, 1
c = int(input("enter range: "))
print(a, b, end=" ")
for i in range(c - 2):
    d = a + b
    a, b = b, d
    print(d, end=" ")
