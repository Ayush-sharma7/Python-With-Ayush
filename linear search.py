l = []
a = int(input("enter no of elements="))
for i in range(0, a):
    b = int(input("enter a value="))
    l.append(b)
print(l)
x = int(input("enter a value to search:"))
for i in range(0, a):
    if l[i] == x:
        print("given no found at position:", i + 1)
        break
else:
    print("given no not found")
